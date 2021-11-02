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
$ python bookccw <crawler_name>
```
, onde `crawler_name` é o nome dos crawlers disponíveis.

### Crawlers Disponíveis
- [x] BaseCrawler
- [ ] BFSCrawler
- [ ] HeuristicCrawler

Os crawlers marcados são os que foram testados e estão funcionando na branch `crawler`.


## Dependencias 

* [Python3](https://www.python.org/)
* [urllib2](https://docs.python.org/3/howto/urllib2.html)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [logging](https://docs.python.org/3/library/logging.html)

## Resolução de Problemas

* [Problema de acesso com o User-Agent](https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request)
* [Criando o parser para o robots.txt](https://stackoverflow.com/questions/60800033/parse-allowed-and-disallowed-parts-of-robots-txt-file)
* [Robots.txt std](http://www.robotstxt.org/robotstxt.html)
* [Syntax obscura do Robots.txt](https://www.ctrl.blog/entry/arcane-robotstxt-directives.html)
* [InvalidSchema no Requests.get](https://stackoverflow.com/questions/30770213/no-schema-supplied-and-other-errors-with-using-requests-get)
* [URL valida](https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python)