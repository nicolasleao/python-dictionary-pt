import peewee

from database import models

word = models.Any


def get_match(text):
    """Returns a word instance in the dictionary, selected by a perfect String match"""
    # Try to find a matching word
    try:
        result = word.get(word.text == text)
        return result
    except peewee.DoesNotExist:
        return None


def get_simple_match(text):
    """Returns a word instance in the dictionary, selected by a simplified String match"""
    # Try to find a matching word
    try:
        result = word.get(word.normalized_text == text)
        return result
    except peewee.DoesNotExist:
        return None


def get_prefix_match(text):
    """Returns a list of words that that have a certain prefix"""
    try:
        result = word.select().where(word.text.startswith(text))
        return list(result)
    except peewee.DoesNotExist:
        return None


def get_simple_prefix_match(text):
    """Returns a list of words that that have a certain prefix"""
    try:
        result = word.select().where(word.normalized_text.startswith(text))
        return list(result)
    except peewee.DoesNotExist:
        return None


def get_suffix_match(text):
    """Returns a list of words that that have a certain prefix"""
    try:
        result = word.select().where(word.text.endswith(text))
        return list(result)
    except peewee.DoesNotExist:
        return None


def get_simple_suffix_match(text):
    """Returns a list of words that that have a certain prefix"""
    try:
        result = word.select().where(word.normalized_text.endswith(text))
        return list(result)
    except peewee.DoesNotExist:
        return None
