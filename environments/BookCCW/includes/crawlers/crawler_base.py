import includes.common.utils as utils
import includes.database.database as db
import requests
import socket
import random
import re
from bs4 import BeautifulSoup

class RobotsParser:
    text = ""
    permitions = {}
    _request_rate = {}
    _crawl_delay = {}
    _site_maps = []

    def __init__(self, text):
        self.text = text
        self.permitions = {"*": {"Allowed": [], "Disallowed": []}}
        self.parse()

    def set_text(self, text):
        self.text = text
        self._request_rate = {}
        self._crawl_delay = {}
        self._site_maps = []
        self.permitions = {"*": {"Allowed": [], "Disallowed": []}}
        self.parse()
    
    def parse(self):
        # User-agents can be chained so i need to keep all in a same chuck to save allowed and disallowed urls
        user_agents = []
        new_chuck = True

        for line in self.text.split("\n"):
            # Removing some white spaces like " Disallow: /    \n"
            line = line.strip()

            if len(line) > 0:
                tag_and_value = line.split(":")
                
                tag = tag_and_value[0].strip() # Here we have "Allow", "Disallow", "User-agent", etc
                
                if (len(tag_and_value) > 1):
                    value = tag_and_value[1].strip() # Here we have the "url_path # Some possible comment"
                else:
                    value = ""

                if tag.startswith("User-agent"):
                    if new_chuck:
                        user_agents = []
                        new_chuck = False
                    
                    user_agents.append(value)
                else:
                    new_chuck = True

                    if tag.startswith('Allow'):
                        possible_url = value.split(" ") # Removes possible spaces with comments
                        if len(possible_url) >= 1:
                            possible_url = possible_url[0]
                            for agent in user_agents:
                                if agent not in self.permitions:
                                    self.permitions[agent] = {"Allowed": [], "Disallowed": []}
                                self.permitions[agent]["Allowed"].append(possible_url)   
                
                    if tag.startswith('Disallow'):
                        possible_url = value.split(" ") # Removes possible spaces with comments
                        if len(possible_url) >= 1:
                            possible_url = possible_url[0]
                            for agent in user_agents:
                                if agent not in self.permitions:
                                    self.permitions[agent] = {"Allowed": [], "Disallowed": []}
                                self.permitions[agent]["Disallowed"].append(possible_url)    

                    if tag.startswith("Crawl-delay"):
                        possible_delay = value.split(" ") # Removes possible spaces with comments
                        if len(possible_delay) >= 1:
                            possible_delay = possible_delay[0]
                            for agent in user_agents:
                                self._crawl_delay[agent] = float(possible_delay)   

                    if tag.startswith("Request-rate"):
                        possible_rate = value.split(" ") # Removes possible spaces with comments
                        if len(possible_rate) >= 1:
                            possible_rate = possible_rate[0]
                            for agent in user_agents:
                                self._request_rate[agent] = possible_rate 

                    if tag.startswith("Sitemaps"):
                            possible_url = value.split(" ") # Removes possible spaces with comments
                            if len(possible_url) >= 1:
                                possible_url = possible_url[0]
                                self._site_maps.append(possible_url) 

                                
    def can_fetch(self, user_agent, path):
        for (agent, permition) in self.permitions.items():
            user_pattern = re.compile(agent.replace("*", ".*"))
            if user_pattern.match(user_agent):
                for url in permition["Disallowed"]:
                    pattern = re.compile(url.replace("*", ".*"))
                    if pattern.match(path):
                        return False
        return True

    def site_maps(self):
        return self._site_maps

    def crawl_delay(self, user_agent):
        if user_agent in self._crawl_delay:
            return self._crawl_delay[user_agent]
        else:
            return None
    
    def request_rate(self, user_agent):
        if user_agent in self._request_rate:
            return self._request_rate[user_agent]
        else:
            return None

class BaseCrawler:
    name = "BaseCrawler"
    path_domain = ""
    path_database = ""
    database = None
    robots = None
    domains = []
    viewed_links = {}
    download_pages = 0
    max_download_pages = 1000

    def __init__(self, path_to_domain_file, path_to_database, max_download_pages = 1000):
        self.path_domain = path_to_domain_file
        self.path_database = path_to_database
        self.max_download_pages = max_download_pages
        self.database = db.Database(self.path_database)
        self.robots = []
        self.domains = self.get_domains()
        self.download_pages = 0
        self.database.expand_db("/" + self.name)

    def is_html(self, response):
        return response.headers['Content-Type'].startswith('text/html')


    def get_fake_user_agent(self):
        UAS = ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"
        ]

        return UAS[random.randrange(len(UAS))]

    def get_pages_robots(self):
        self.database.expand_db("/" + self.name + "/robots")
        for url in self.domains:
            headers = {"User-Agent": self.get_fake_user_agent()}
            site = requests.get(url + "/robots.txt", headers=headers)
            self.database.save_robots_file(self.path_database + "/"+ self.name +"/robots/robots_to_" + str(utils.get_domain_main_name(url)), site.text)
            self.robots.append(RobotsParser(site.text))

    def get_domains(self):
        return utils.names_list_from_file(self.path_domain)

    def crawl(self):
        pass

    def save_page(self, path_to_db_dir, page_url, page_content):
        if self.download_pages < self.max_download_pages:

            db_obj = db.DatabaseObj(path_to_db_dir + "/" + str(self.download_pages), page_url, page_content)

            self.database.save_file(db_obj)

            self.download_pages += 1

            if self.download_pages >= self.max_download_pages:
                return False
            else:
                return True
        else:
            return False