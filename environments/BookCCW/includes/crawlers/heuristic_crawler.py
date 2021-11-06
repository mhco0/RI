from includes.crawlers.crawler_base import *
import heapq

class HeuristicCrawler(BaseCrawler):
    name = "HeuristicCrawler"
    url_heap = []
    rank_func = lambda x : 1

    def __init__(self,  path_to_domain_file, path_to_database, max_download_pages = 1000):
        super().__init__(path_to_domain_file, path_to_database, max_download_pages)

    def set_heuristic_function(self, f):
        self.rank_func = f

    def crawl(self):
        self.get_pages_robots()
        for i in range(len(self.domains)):
            domain_main_name = str(utils.get_domain_main_name(self.domains[i]))
            self.database.expand_db("/" + self.name + "/" + domain_main_name)
            headers = {"User-Agent": self.get_fake_user_agent()}
            self.download_pages = 0
            self.url_heap = []
            heapq.heappush(self.url_heap, (1, self.domains[i]))
            self.viewed_links[self.domains[i]] = True
            session = requests.Session()

            while(len(self.url_heap) != 0):
                (_, front_url) = heapq.heappop(self.url_heap)
                if not front_url.startswith("http"):
                    continue

                print(front_url)
                
                try:
                    page = session.get(front_url, headers=headers, timeout=5)
                except:
                    continue

                if(page.status_code == 200 and self.is_html(page)):
                    soup = BeautifulSoup(page.content, 'html.parser')

                    for link in soup.find_all('a'):                   
                        new_url = link.get('href')
                        if new_url != None:
                            if self.robots[i].can_fetch(headers["User-Agent"], new_url) and new_url not in self.viewed_links:
                                self.viewed_links[new_url] = True
                                if new_url.startswith("/"):
                                    new_url = self.domains[i] + new_url

                                
                                rank = self.rank_func(new_url)
                                anchor = link.text
                                if anchor != None:
                                    rank += self.rank_func(anchor)

                                heapq.heappush(self.url_heap, (-rank, new_url))

                    if not self.save_page(self.path_database + "/" + self.name + "/" + domain_main_name, front_url, page.text):
                        break