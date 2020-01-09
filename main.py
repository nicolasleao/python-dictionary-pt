from crawler import crawler
from database import models
from util import util, selectors

# General behaviour variables
debug = True
crawl = False

if __name__ == '__main__':
    if crawl:
        util.create_tables()
        crawler.crawl(models.Verbete, 'https://dicionario.aizeta.com/verbetes/todos/')
    else:
        command = None
        while not command == "exit":
            command = input("query> ")
            for item in selectors.get_simple_prefix_match(command):
                print(item.normalized_text)
