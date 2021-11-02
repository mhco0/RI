from includes.crawlers.crawler_base import *
from includes.crawlers.bfs_crawler import *
from includes.crawlers.heuristic_crawler import *
import http.client
import logging
import sys

DOMAIN_FILE_PATH = "includes/common/dominios2"
DATABASE_PATH = "includes/database/db"
PAGES_TO_DOWNLOAD = 1000

if __name__ == "__main__":
    http.client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    if len(sys.argv) > 1:
        crawler_type = sys.argv[1]
        test_crawler = None

        if crawler_type == "BFSCrawler":
            test_crawler = BFSCrawler(DOMAIN_FILE_PATH, DATABASE_PATH, PAGES_TO_DOWNLOAD)
        elif crawler_type == "HeuristicCrawler":
            test_crawler = HeuristicCrawler(DOMAIN_FILE_PATH, DATABASE_PATH, PAGES_TO_DOWNLOAD)
        else:
            test_crawler = BaseCrawler(DOMAIN_FILE_PATH, DATABASE_PATH, PAGES_TO_DOWNLOAD)

        test_crawler.crawl()