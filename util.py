import peewee
import unidecode

from database import models


def create_tables():
    try:
        models.Verbo.create_table()
        print("'Verbo' table created successfully!")
    except peewee.OperationalError:
        print("'Verbo' table already exists!")

    try:
        models.Substantivo.create_table()
        print("'Substantivo' table created successfully!")
    except peewee.OperationalError:
        print("'Substantivo' table already exists!")

    try:
        models.Adjetivo.create_table()
        print("'Adjetivo' table created successfully!")
    except peewee.OperationalError:
        print("'Adjetivo' table already exists!")

    try:
        models.Adverbio.create_table()
        print("'Adverbio' table created successfully!")
    except peewee.OperationalError:
        print("'Adverbio' table already exists!")


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


def format_string(source_string):
    # convert utf-8 to ascii text
    result = unidecode.unidecode(source_string).lower()
    return result
