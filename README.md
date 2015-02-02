candidates2014
==============

Scrappers that grab declarations and biographies of the MPs candidates in Ukrainian parliament - Elections 2014

## add_ids_to_filenames.py
Script that finds MP's chesno ID for all [.pdf] files in a working directory.
Requires [transliterate](https://pypi.python.org/pypi/transliterate) to convert names with latin characters and [python-Levenshtein](https://pypi.python.org/pypi/python-Levenshtein/).
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

## get_photos.py
Downloads MP photos from the list on rada.gov.ua to the working directory.
Requires [PyQuery](https://pypi.python.org/pypi/pyquery) and [httplib2](https://pypi.python.org/pypi/httplib2).

These photos can be further processed with
```
add_ids_to_filenames.py --extension=".jpg" --rename
add_ids_to_filenames.py --extension=".jpg" --full-rename --rename
```

## get_assistants.py
Prints list of assistants for every MP along with their IDs and names to the stdout.
Usage:
```
python3 get_assistants.py > assistants.csv
```

## mp_base.py
Helper class to work with MP database.