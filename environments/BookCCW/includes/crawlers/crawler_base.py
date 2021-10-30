import urllib.request
import urllib.robotparser as urobot
import urllib.request
import includes.common.utils as utils
import includes.database.database as database
import requests
import socket
from bs4 import BeautifulSoup

# Test for function to check robots.txt use this later
def dummy():
    url = "example.com"
    rp = urobot.RobotFileParser()
    rp.set_url(url + "/robots.txt")
    rp.read()
    if rp.can_fetch("*", url):
        site = urllib.request.urlopen(url)
        sauce = site.read()
        soup = BeautifulSoup(sauce, "html.parser")
        actual_url = site.geturl()[:site.geturl().rfind('/')]

        my_list = soup.find_all("a", href=True)
        for i in my_list:
            # rather than != "#" you can control your list before loop over it
            if i != "#":
                newurl = str(actual_url)+"/"+str(i)
                try:
                    if rp.can_fetch("*", newurl):
                        site = urllib.request.urlopen(newurl)
                        # do what you want on each authorized webpage
                except:
                    pass
    else:
        print("cannot scrap")

class BaseCrawler:
    name = "BaseCrawler"
    path_domain = "BookCCW/includes/common/dominios"
    robot_parser = None
    viewed_links = {}
    forbidden_links = {}

    def __init__(self, path_to_domain_file):
        self.path_domain = path_to_domain_file
        self.robot_parser = urobot.RobotFileParser()

    def set_robots_verification(self, url):
        self.robot_parser.set_url(url + "/robots.txt")
        self.robot_parser.read()

    def can_fetch(self, url):
        return self.robot_parser.can_fetch("*", url)

    def crawl(self):
        urls = utils.names_list_from_file(self.path_domain)
        for url in urls:
            self.viewed_links[url] = True
            #self.set_robots_verification(url)
            #if self.can_fetch(url):
                #site = urllib.request.urlopen(url)
            headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
            site = requests.get(url, headers=headers)
            print(site)
                
            #else:
            #    print("oxi")

    def save_html(self, response):
        filename = f'domain-{response.url.split(".")[1]}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

    def process_response(self, response):
        if response.headers['Content-Type'] != 'text/html':
            return
        else:
            save_html(response)
