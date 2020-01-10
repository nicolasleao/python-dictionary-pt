import peewee
import unidecode

from database import models


def create_tables():
    try:
        models.Any.create_table()
        print("'any' table created successfully!")
    except peewee.OperationalError:
        print("'any' table already exists!")

    try:
        models.Verb.create_table()
        print("'verb' table created successfully!")
    except peewee.OperationalError:
        print("'verb' table already exists!")

    try:
        models.Noun.create_table()
        print("'noun' table created successfully!")
    except peewee.OperationalError:
        print("'noun' table already exists!")

    try:
        models.Adjective.create_table()
        print("'adjective' table created successfully!")
    except peewee.OperationalError:
        print("'adjective' table already exists!")

    try:
        models.Adverb.create_table()
        print("'adverb' table created successfully!")
    except peewee.OperationalError:
        print("'adverb' table already exists!")


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


def normalize_text(source_string):
    # convert utf-8 to ascii text
    result = unidecode.unidecode(source_string).lower()
    return result


def normalize_meaning(source_string):
    """Escape all HTML tags if any"""

    flag = 0
    index = 0

    # Trash is a list containing all the html tags found in the source string
    trash = []
    for c in source_string:
        if c == '<':
            # Flag the start of the html tag
            flag = index
        elif c == '>':
            # Append full tag from the flagged start to the current index
            trash.append(source_string[flag:index+1])
        index += 1

    # Remove whitespaces from start and end of string
    result = source_string.strip()

    # Remove all html tags inside the trash variable
    for item in trash:
        result = result.replace(item, '')

    # Return normalized string
    return result

