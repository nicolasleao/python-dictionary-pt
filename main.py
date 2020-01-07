import util
from crawler import crawler
from database import models
import peewee

debug = True
crawl = True


if __name__ == '__main__':
    if crawl:
        util.create_tables()
        crawler.crawl(models.Substantivo, 'https://dicionario.aizeta.com/verbetes/substantivo/')
        crawler.crawl(models.Adjetivo, 'https://dicionario.aizeta.com/verbetes/adjetivo/')
        crawler.crawl(models.Verbo, 'https://dicionario.aizeta.com/verbetes/verbo/')
        crawler.crawl(models.Adverbio, 'https://dicionario.aizeta.com/verbetes/adverbio/')
    else:
        command = None
        while not command == "exit":
            command = input("Command> ")
            if command == 'get':
                text = input("Query> ")
                try:
                    result = models.BaseModel.get(models.BaseModel.text == text)
                    print(result.meaning)
                except:
                    print('Instance not found')