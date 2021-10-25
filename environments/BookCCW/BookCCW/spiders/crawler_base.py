import scrapy
import BookCCW.includes.common.utils as utils

class BaseCrawler(scrapy.Spider):
    name = "BaseCrawler"
    file = "BookCCW/includes/common/dominios"
    count_domain = 0

    def start_requests(self):
        urls = utils.names_list_from_file(self.file)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def process_response(self, response):
        self.count_domain += 1
        filename = f'domain-{self.count_domain}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

    def parse(self, response):
        self.process_response(response)
