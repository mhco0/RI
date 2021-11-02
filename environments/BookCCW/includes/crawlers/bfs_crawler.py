from includes.crawlers.crawler_base import *

class BFSCrawler(BaseCrawler):
    name = "BFSCrawler"
    url_queue = []

    def __init__(self,  path_to_domain_file, path_to_database, max_download_pages = 1000):
        super().__init__(path_to_domain_file, path_to_database, max_download_pages)

    def crawl(self):
        self.get_pages_robots()
        for i in range(len(self.domains)):
            domain_main_name = str(utils.get_domain_main_name(self.domains[i]))
            self.database.expand_db("/" + self.name + "/" + domain_main_name)
            headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
            self.download_pages = 0
            self.url_queue = []
            self.url_queue.append(self.domains[i])
            self.viewed_links[self.domains[i]] = True
            session = requests.Session()

            while(len(self.url_queue) != 0):
                front_url = self.url_queue.pop(0)
                if not front_url.startswith("http"):
                    continue

                print(front_url)
                try:
                    page = session.get(front_url, headers=headers, timeout=5)
                except:
                    continue
                print(page)
                print(page.headers)
                print(page.content)
                print(page.text)
                if(page.status_code == 200 and self.is_html(page)):
                    soup = BeautifulSoup(page.content, 'html.parser')

                    print(soup.find_all('a'))
                    for link in soup.find_all('a'):                                    
                        new_url = link.get('href')
                        if new_url != None:
                            if self.robots[i].can_fetch(headers["User-Agent"], new_url) and new_url not in self.viewed_links:
                                self.viewed_links[new_url] = True
                                if new_url.startswith("/"):
                                    new_url = self.domains[i] + new_url
                                self.url_queue.append(new_url)

                    if not self.save_page(self.path_database + "/" + self.name + "/" + domain_main_name, front_url, page.text):
                        break
               
