#!/usr/bin/python3
# Copyright 2014 Serhiy Zahoriya
# GPLv3

from Levenshtein import distance
from transliterate import translit

from sys import argv, stderr, exit
from csv import reader
from os import listdir, rename, path
from argparse import ArgumentParser

BASE_LOCATION = '../../base.csv'
START_DIST = 3
NONAME_PREFIXES = {'decl', 'bio'}

parser = ArgumentParser()

parser.set_defaults(
	party=None,
	simulate=True,
	name_reversed=False,
	extension=".pdf",
	full_rename=False)

parser.add_argument(
	"--party",
	help="search only this party members, exact name")

parser.add_argument(
	"--rename",
	help="disable simulation mode",
	dest="simulate",
	action="store_false")

parser.add_argument(
	"--name-reversed",
	help="first and last names switched",
	dest="name_reversed",
	action="store_true")

parser.add_argument(
	"--extension",
	help="only affect these files, defaults to .pdf")

parser.add_argument(
	"--full-rename",
	help="use name from database",
	dest="full_rename",
	action="store_true")

args = parser.parse_args()


def find_similar_names(search_name, base, default_distance):
	similar_names = list()
	for mpid in base.keys():
		# mpid, name, link, party, ticket, district,\
		# rid, rdate, urid, urdate, urreason,\
		# bio, profile, party12, ticket12, link12,\
		# district12, did12, dlink12, loh, lohcom,\
		# corrupt, autobio, biolink, decl, decllink

		name = base[mpid][1]
		district = base[mpid][5]

		dist = list()
		for pair in zip(search_name, name):
			search_name_el, name_el = pair
			if len(search_name_el) == 1:
				name_el = name_el[0:1]
			current_dist = distance(search_name_el, name_el)
			dist.append(current_dist)

		if len(search_name) == len(name) and sum(dist) == 0:
			return [[mpid, name, district]]

		if all(d < default_distance for d in dist):
			similar_names.append([mpid, name, district])
	return similar_names


def _rename(old_filename, new_filename):
	print("	", file, "	>	", new_filename, '\n')
	if not args.simulate:
		rename(old_filename, new_filename)


# Reading CSV
with open(BASE_LOCATION) as basefile:
	csv_reader = reader(basefile)
	next(csv_reader)
	csv_list = list(csv_reader)

base = dict()
for row in csv_list:
	if args.party and row[3] != args.party:
		continue
	mpid = int(row[0])
	if mpid in base.keys():
		print("Duplicate MP ID in database: " + str(mpid), file=stderr)
		# exit(1)
	base[mpid] = row
	base[mpid][1] = base[mpid][1].lower().replace(" ", "_").split("_")

# Work with files
for file in listdir('.'):
	# Skip files that don't have needed extension
	if not file.lower().endswith(args.extension):
		continue

	search_name = path.splitext(file)[0].split("_")

	# Skip files that have ids
	got_id = None
	try:
		got_id = int(search_name[0])
		search_name.pop(0)
	except:
		pass

	# Skip type prefixes
	prefix = ""
	if search_name[0] in NONAME_PREFIXES:
		prefix = search_name.pop(0) + "_"

	if got_id:
		if not args.full_rename:
			continue
		new_filename = \
			str(got_id) + '_'\
			+ prefix\
			+ '_'.join([
					translit(el, 'uk', reversed=True)
					for el in base[got_id][1]])\
			+ args.extension
		_rename(file, new_filename)
		continue

	print(file)

	search_name = [translit(el, 'uk') for el in search_name]
	if args.name_reversed:
		search_name[0], search_name[1] = search_name[1], search_name[0]

	similar_names = list()
	current_dist = START_DIST
	while not similar_names:
		similar_names = find_similar_names(search_name, base, current_dist)
		current_dist += 1

	if len(similar_names) > 1:
		# TODO: sort by distance?
		namesakes = list()

		for cand in similar_names:
			name = cand[1]
			if distance(search_name[0], name[0]) == 0:
				namesakes.append(cand)

		if len(namesakes) == 1:
			similar_names = namesakes
			selected = 0

		else:
			for i in range(len(similar_names)):
				mpid, name, district = similar_names[i]
				print(
					str(i + 1) + ")	",
					mpid,
					' ',
					' '.join([el.title() for el in name]),
					'	',
					district)
			try:
				selected = int(input("№:")) - 1
			except:
				print('SKIPPED\n')
				continue
	else:
		selected = 0

	file_id = similar_names[selected][0]
	new_filename = str(file_id) + '_' + file
	_rename(file, new_filename)
