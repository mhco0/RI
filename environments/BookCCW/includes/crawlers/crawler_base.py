import urllib.request
import urllib.robotparser as urobot
import urllib.request
import BookCCW.includes.common.utils as utils
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
    file = "BookCCW/includes/common/dominios"
    viewed_links = {}
    forbidden_links = {}

    def start_requests(self):
        urls = utils.names_list_from_file(self.file)
        for url in urls:
            viewed_links[url] = True
            #yield scrapy.Request(url=url, callback=self.parse)
            # Change here for Request

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
