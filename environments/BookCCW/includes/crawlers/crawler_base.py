import includes.common.utils as utils
import includes.database.database as db
import requests
import socket
import random
from bs4 import BeautifulSoup

class BaseCrawler:
    name = "BaseCrawler"
    path_domain = ""
    path_database = ""
    database = None
    robots_parser = None
    viewed_links = {}
    forbidden_links = {}

    def __init__(self, path_to_domain_file, path_to_database, max_download_pages = 1000):
        self.path_domain = path_to_domain_file
        self.path_database = path_to_database
        self.max_download_pages = max_download_pages
        self.database = db.Database(self.path_database)
        self.robots_response = None

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
        urls = utils.names_list_from_file(self.path_domain)
        self.database.expand_db("/robots")
        domain_count = 0
        for url in urls:
            headers = {"User-Agent": self.get_fake_user_agent()}
            site = requests.get(url + "/robots.txt", headers=headers)
            self.database.save_file(db.DatabaseObj(self.path_database + "/robots/robot_to_domain_" + str(domain_count), url, site.text))
            domain_count += 1

    def crawl(self):
        urls = utils.names_list_from_file(self.path_domain)
        for url in urls:
            self.viewed_links[url] = True
            headers = {"User-Agent": self.get_fake_user_agent()}
            site = requests.get(url, headers=headers)

