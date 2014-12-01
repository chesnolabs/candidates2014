#!/usr/bin/python3

from pyquery import PyQuery as pq
from httplib2 import Http

LIST_URL = 'http://w1.c1.rada.gov.ua/pls/site2/fetch_mps?skl_id=9'
LIST_ELEMENT = 'ul.search-filter-results-thumbnails li'
ELEMENT_IMG = 'p.thumbnail img'
ELEMENT_NAME_TAG = 'p.title a'
EXT = ".jpg"

USERAGENT = "Mozilla/5.0 (X11; Linux i686) (KHTML, Gecko) Chrome/40.0.1234.56"

http = Http('.cache', timeout=10)
q = pq(url=LIST_URL)


def download(url, filename):
	try:
		response, content = http.request(url, headers={'User-Agent': USERAGENT})

		with open(filename, 'wb') as filehandler:
			filehandler.write(content)
	except Exception as e:
		print(str(e))


for dep in q(LIST_ELEMENT):
	depq = pq(dep)
	photo = depq(ELEMENT_IMG).attr('src')
	name = depq(ELEMENT_NAME_TAG).text()
	print(photo, name.replace(" ", "_") + EXT)
	download(photo, name.replace(" ", "_") + EXT)
