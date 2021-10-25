from BookCCW.spiders.crawler_base import *

class BFSCrawler(BaseCrawler):
    name = "BFSCrawler"

    def process_response(self, response):
        print(response)