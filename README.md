candidates2014
==============

Scrappers that grab declarations and biographies of the MPs candidates in Ukrainian parliament - Elections 2014

## add_ids_to_filenames.py
Script that finds MP's chesno ID for all files in a working directory.
Uses [transliterate](https://pypi.python.org/pypi/) to convert names with latin characters and [python-Levenshtein](https://pypi.python.org/pypi/python-Levenshtein/).
Assumes that MPs database is in `../../base.csv`

Usage:
```
python3 ../../candidates2014/add_ids_to_filenames.py # verify changes
python3 ../../candidates2014/add_ids_to_filenames.py --rename
python3 ../../candidates2014/add_ids_to_filenames.py --party="`cat ../party_name.txt`" --extension=".html"
```
Input filenames examples:
```
прізвище.pdf
decl_прізвище.pdf
bio_прізвище.pdf
прізвище_ім’я_по-батькові.pdf
прізвище_і_б.pdf
ім’я_прізвище.pdf (with --name-reversed)
```
All files starting with an integer and underscore will be ignored.
