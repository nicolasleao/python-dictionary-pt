from string import ascii_lowercase

import requests

debug = True


def get_substrings(source_string, start, end):
    """Returns a list of substrings that are found inside 'str' between the 'start' string and 'end' string"""
    substrings = []
    current_pos = 0
    str_length = len(source_string)
    running = True

    # Keep looping while the current index position is less than the string length, and running is True
    while current_pos < str_length and running == True:
        int_index1 = source_string.find(start, current_pos)
        if int_index1 != -1:
            # The prefix was found, mark the index and proceed
            int_index1 = int_index1 + len(start)
            int_index2 = source_string.find(end, int_index1)
            if int_index2 != -1:
                # The prefix was found, mark the index and append string between start and end indexes
                subsequence = source_string[int_index1:int_index2]
                substrings.append(subsequence)
                # the new starting index is the suffix's index + suffix string length
                current_pos = int_index2 + len(end)
            else:
                # If the suffix was not found, stop function loop
                running = False
        else:
            # If the prefix was not found, stop function loop
            running = False
    return substrings


def crawl(filename, url):
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

    letters = ascii_lowercase

    # Open file to write results
    with open(filename, 'w') as f:
        # Iterate through the whole alphabet
        for c in letters:
            # Append current letter to url, and start from page 1
            current_page = 1
            current_url = url + c + '/'
            response = requests.get(current_url + str(current_page), headers=headers)
            result = get_substrings(response.text, search_prefix, search_suffix)
            # Append current page to url
            while result:
                if debug:
                    print(result)
                # Update current page and url string
                current_page += 1
                new_current_url = current_url + str(current_page)
                if debug:
                    print(new_current_url)

                # Append current results to file
                for item in result:
                    f.write("%s\n" % item)

                # Fetch results from next page
                response = requests.get(new_current_url, headers=headers)
                result = get_substrings(response.text, search_prefix, search_suffix)


if __name__ == '__main__':
    crawl('substantivos.txt', 'https://dicionario.aizeta.com/verbetes/substantivo/')
    crawl('adjetivos.txt', 'https://dicionario.aizeta.com/verbetes/adjetivo/')
    crawl('verbos.txt', 'https://dicionario.aizeta.com/verbetes/verbo/')
    crawl('adverbios.txt', 'https://dicionario.aizeta.com/verbetes/adverbio/')
