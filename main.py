import util
from crawler import crawler
from database import models

debug = True


if __name__ == '__main__':
    util.create_tables()

    crawler.crawl(models.Substantivo, 'https://dicionario.aizeta.com/verbetes/substantivo/')
    crawler.crawl(models.Adjetivo, 'https://dicionario.aizeta.com/verbetes/adjetivo/')
    crawler.crawl(models.Verbo, 'https://dicionario.aizeta.com/verbetes/verbo/')
    crawler.crawl(models.Adverbio, 'https://dicionario.aizeta.com/verbetes/adverbio/')
