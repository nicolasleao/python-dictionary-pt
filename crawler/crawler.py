from string import ascii_lowercase

import peewee
import requests

import dictionary
from util import util

debug = dictionary.debug


def crawl(model, url):
    """Loops through all pages of the site and add words to database"""

    # Fake user-agent to bypass firewall
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

            # Insert results on database
            counter = 0
            for item in result:
                normalized_text = util.normalize_text(item)
                try:
                    # Try to get the meanings for the current word
                    meaning_url = 'https://dicionario.aizeta.com/significado/' + normalized_text
                    meaning_prefix = '<blockquote>'
                    meaning_suffix = '</blockquote>'
                    meaning_response = requests.get(meaning_url, headers=headers)
                    meanings = util.get_substrings(meaning_response.text, meaning_prefix, meaning_suffix)

                    if meanings:
                        normalized_meaning = util.normalize_meaning(meanings[0])
                        print(normalized_meaning)
                        model.create(text=item, normalized_text=normalized_text, meaning=normalized_meaning)
                    else:
                        model.create(text=item, normalized_text=normalized_text, meaning="")
                except peewee.IntegrityError:
                    pass
                counter += 1

            # Fetch results from next page
            response = requests.get(new_current_url, headers=headers)
            result = util.get_substrings(response.text, search_prefix, search_suffix)
