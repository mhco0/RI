# RI
Projeto de RI

## Crawlers

### Como rodar
Todo o projeto está dentro de uma [máquina virtual](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-20-04) de python.

Para entrar no ambiente virtual, execute:
```
$ cd environments
$ . env/bin/activate // ou source env/bin/activate
```

Para testar algum Crawler basta digitar o seguinte comando:
```
// Certifique-se de estar dentro da pasta 'RI/environments/BookCCW'
$ scrapy crawl <crawler_name>
```
, onde `crawler_name` é o nome dos crawlers disponíveis.

### Crawlers Disponíveis
- [x] BaseCrawler
- [ ] BFSCrawler
- [ ] HeuristicCrawler

Os crawlers marcados são os que foram testados e estão funcionando na branch `crawler`.
