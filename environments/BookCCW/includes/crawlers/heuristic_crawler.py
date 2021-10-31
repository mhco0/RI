from includes.crawlers.crawler_base import *

class HeuristicCrawler(BaseCrawler):
    name = "HeuristicCrawler"

    def process_response(self, response):
        print(response)