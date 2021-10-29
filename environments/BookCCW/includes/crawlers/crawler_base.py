import urllib.request
import BookCCW.includes.common.utils as utils

class BaseCrawler:
    name = "BaseCrawler"
    file = "BookCCW/includes/common/dominios"
    viewed_links = {}
    forbidden_links = {}

    def start_requests(self):
        with urllib.request.urlopen('http://python.org/') as response:
            html = response.read()

        urls = utils.names_list_from_file(self.file)
        for url in urls:
            viewed_links[url] = True
            yield scrapy.Request(url=url, callback=self.parse)

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

    def parse(self, response):
        self.process_response(response)
