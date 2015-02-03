#!/usr/bin/python3
# Copyright 2015 Serhiy Zahoriya
# GPLv3

from pyquery import PyQuery as pq
from httplib2 import Http
from sys import stderr
from time import sleep
from mp_base import MPBase

LIST_URL = 'http://w1.c1.rada.gov.ua/pls/site2/fetch_mps?skl_id=9'
LIST_ELEMENT = 'ul.search-filter-results-thumbnails li p.title a'

MP_NAME_SELECTOR = "#mp_content table.simple_info h2"
ASSISTANTS_TITLE_START = "ПОМІЧНИКИ-КОНСУЛЬТАНТИ"

USERAGENT = "Mozilla/5.0 (X11; Linux i686) (KHTML, Gecko) Chrome/40.0.1234.56"


def get_assistants(mp_page_url, base):
    page_downloaded = False
    while not page_downloaded:
        try:
            q = pq(url=mp_page_url, headers={'user-agent': USERAGENT})
            page_downloaded = True
        except:
            continue

    mp_name = q(MP_NAME_SELECTOR).text()
    mp_id = base.get_mp_id_by_name(mp_name)

    assistants = []
    in_assistants_list = False

    for div in [q(div) for div in q("div")]:
        if div.text().upper().startswith(ASSISTANTS_TITLE_START): 
            in_assistants_list = True
            continue

        if in_assistants_list:
            if div.attr('style') \
            and div.attr('style').startswith('clear: both;'):
                in_assistants_list = False
                break

            assistant_reason = div.children('span').text().strip(':')
            for assistant_name in div.remove('span').text().split(","):
                assistant_name = assistant_name.strip()
                print(','.join([
                                mp_id,
                                mp_name,
                                assistant_name,
                                assistant_reason]))


if __name__ == '__main__':
    main_list = pq(url=LIST_URL, headers={'user-agent': USERAGENT})
    base = MPBase()

    for mp_page_url in [pq(mp).attr('href') for mp in main_list(LIST_ELEMENT)]:
        print(mp_page_url, file=stderr)
        get_assistants(mp_page_url, base)
        sleep(3)

