import crawler_base

class HeuristicCrawler(BaseCrawler):
    name = "HeuristicCrawler"

    def process_response(self, response):
        print(response)