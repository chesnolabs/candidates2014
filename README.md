candidates2014
==============

Scrappers that grab declarations and biographies of the MPs candidates in Ukrainian parliament - Elections 2014

## add_ids_to_filenames.py
Script that finds MP's chesno ID for all files in a working directory. Input filenames examples:

```
прізвище_ім’я_по-батькові.pdf
прізвище_і_б.pdf
прізвище.pdf
decl_прізвище[_ім’я_по-батькові].pdf
bio_прізвище[_ім’я_по-батькові].pdf
```

All files starting with an integer and underscore will be ignored.

Uses [transliterate](https://pypi.python.org/pypi/) to convert names with latin characters and [python-Levenshtein](https://pypi.python.org/pypi/python-Levenshtein/).
