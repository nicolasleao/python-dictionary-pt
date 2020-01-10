# python-pt-dictionary
A brazilian portuguese dictionary stored in an SQLite database for fast querying.
The words in this dictionary and their meanings were collected from the [AIZETA](https://dicionario.aizeta.com/) 
dictionary by a [web crawler](./crawler/crawler.py).

## Installation
The installation process is very simple, since the whole project is a python package, you can simply clone this repository
inside your project:
```shell script
git clone https://github.com/nicolasleao/python_pt_dictionary.git
pip install -r python_pt_dictionary/requirements.txt
```

Once the installation is complete, you can import the package inside your project using:
```python
from python_pt_dictionary import dictionary
```
## Usage
There are 6 available query types, you can query using the whole word, using a prefix, or using a suffix, all of these
options can either be queried by a perfect match, including Accentuation, or a simplified match, that ignores accentuation.

to execute a query, use the following command:
```python
dictionary.select('Your query', selector_command)
```

Available selector commands:

selector_command | description
--- | ---
dictionary.Selector.PERFECT | Whole word, perfect match
dictionary.Selector.SIMPLE | Whole word, simplified match
dictionary.Selector.PREFIX | Prefix, perfect match
dictionary.Selector.SIMPLE_PREFIX | Prefix, simplified match
dictionary.Selector.SUFFIX | Suffix, perfect match
dictionary.Selector.SIMPLE_SUFFIX | Suffix, perfect match

Example:

```python
result = dictionary.select("Peixe", dictionary.Selector.PERFECT)
```
will store the instance of the word Peixe, found in the database, inside the 'result' variable,
and
```python
print(result.meaning)
```
Will print "Animal vertebrado que vive na água e respira por guelras."
