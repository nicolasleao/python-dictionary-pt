from string import ascii_lowercase

import peewee
import requests

import util
from database import models

debug = True


def crawl(model, url):
    """Loops through all pages of the site and appends found words to 'wordlist.txt' file"""
    print("Starting site scan")

    # Fake windows 10 mozilla user-agent to bypass firewall
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }

    # This marks the beginning of a word
    search_prefix = "<div class=\"info-feat\"><p><b>"

    # This marks the end of a word
    search_suffix = "</b></p><i>"

    # Iterate through the whole alphabet
    for c in ascii_lowercase:
        # Append current letter to url, and start from page 1
        current_page = 1
        current_url = url + c + '/'
        response = requests.get(current_url + str(current_page), headers=headers)
        result = util.get_substrings(response.text, search_prefix, search_suffix)
        # Append current page to url
        while result:
            # Update current page and url string
            current_page += 1
            new_current_url = current_url + str(current_page)
            if debug:
                print(new_current_url)

            # Insert results on database
            counter = 0
            for item in result:
                normalized_text = util.format_string(item)
                if debug:
                    print(normalized_text)
                try:
                    model.create(text=normalized_text)
                except peewee.IntegrityError:
                    pass
                counter += 1

            if debug:
                print("Added " + str(counter) + " entries to the database.")

            # Fetch results from next page
            response = requests.get(new_current_url, headers=headers)
            result = util.get_substrings(response.text, search_prefix, search_suffix)


if __name__ == '__main__':
    util.create_tables()

    crawl(models.Substantivo, 'https://dicionario.aizeta.com/verbetes/substantivo/')
    crawl(models.Adjetivo, 'https://dicionario.aizeta.com/verbetes/adjetivo/')
    crawl(models.Verbo, 'https://dicionario.aizeta.com/verbetes/verbo/')
    crawl(models.Adverbio, 'https://dicionario.aizeta.com/verbetes/adverbio/')
