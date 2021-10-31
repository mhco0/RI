from includes.crawlers.crawler_base import *
import http.client
import logging


if __name__ == "__main__":
    #http.client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    #logging.basicConfig()
    #logging.getLogger().setLevel(logging.DEBUG)
    #requests_log = logging.getLogger("requests.packages.urllib3")
    #requests_log.setLevel(logging.DEBUG)
    #requests_log.propagate = True
    test_crawler = BaseCrawler("includes/common/dominios", "includes/database/db")
    test_crawler.get_pages_robots()