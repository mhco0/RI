from BookCCW.spiders.crawler_base import *

class BFSCrawler(BaseCrawler):
    name = "BFSCrawler"
    url_queue = []

    def start_requests(self):
        urls = utils.names_list_from_file(self.file)
        for url in urls:
            viewed_links[url] = True
            self.url_queue.append(url)

            while(len(self.url_queue) != 0):
                front_url = self.url_queue.pop(0) 
                yield scrapy.Request(url=front_url, callback=self.parse)
            
            self.count_domain = 0

    def process_response(self, response):
        self.count_domain += 1
        if self.count_domain > 1000 or response.headers['Content-Type'] != 'text/html':
            return

        for link in response.css('a::attr(href)'):

            if not link in self.viewed_link:
                self.viewed_links[link] = True
                self.url_queue.append(link)

        self.save_html(response)
