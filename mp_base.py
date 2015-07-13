#!/usr/bin/python3
# Copyright 2015 Serhiy Zahoriya
# GPLv3

from csv import reader


class MPBase():
    def __init__(self,
                 base_location='../data/mp_id_base.csv',
                 with_header=False,
                 party_filter=None):
        self.base = dict()

        with open(base_location) as base_file:
            csv_reader = reader(base_file)

            if with_header:
                next(csv_reader)

            for row in csv_reader:
                mp_id, mp_name, mp_party = row

                if party_filter and mp_party != party_filter:
                    continue

                self.base[mp_name] = mp_id

    def get_mp_id_by_name(self, mp_name, default=''):
        mp_name = mp_name.replace('\'', '’')
        if mp_name in self.base:
            return self.base[mp_name]
        else:
            return default
