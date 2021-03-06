candidates2014
==============

Scrapers that grab declarations and biographies of the MPs candidates in Ukrainian parliament - Elections 2014


## Installing requirements
```
pip3 install -r requirements.txt
git clone https://github.com/chesnolabs/data ../data
```


## add_ids_to_filenames.py
Script that finds MP's chesno ID for all [.pdf] files in a working directory.

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
All files starting with an integer and underscore will be ignored unless `--full-rename` option is provided in which case it will use the integer as an MP ID and rename the file taking credentials by this ID.


## get_photos.py
Downloads MP photos from the list on rada.gov.ua to the working directory.

These photos can be further processed with
```
add_ids_to_filenames.py --extension=".jpg" --rename
add_ids_to_filenames.py --extension=".jpg" --full-rename --rename
```


## get_assistants.py
Prints list of assistants for every MP along with their names to the stdout.

Usage:
```
python3 get_assistants.py > assistants.csv
```


## mp_base.py
Helper class to work with MP database.
