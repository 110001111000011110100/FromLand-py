# -*- coding: UTF-8 -*-
import re

from constants import ul_patt, per_patt, pass_patt, trakt_patt, ave_patt, road_patt, house_patt, snt_patt


def parse_address(address, data0):
    match = None
    prefix = ''
    postfix = ''

    address = re.sub(r'[№\"()]', '', address)
    address = re.sub(r'участок|земельный участок|уч\.|уч', 'уч.', address)

    if re.search(ul_patt, address):
        postfix = u' улица'
        match = re.search(ul_patt, address)
    elif re.search(per_patt, address):
        postfix = u' переулок'
        match = re.search(per_patt, address)
    elif re.search(pass_patt, address):
        postfix = u' проезд'
        match = re.search(pass_patt, address)
    elif re.search(trakt_patt, address):
        postfix = u' тракт'
        match = re.search(trakt_patt, address)
    elif re.search(ave_patt, address):
        postfix = u' проспект'
        match = re.search(ave_patt, address)
    elif re.search(road_patt, address):
        postfix = u' шоссе'
        match = re.search(road_patt, address)
    elif re.search(snt_patt, address):
        prefix = u'СНТ '
        match = re.search(snt_patt, address)

    try:
        if match:
            street_plus_num = re.split(match.re, address)
            street_and_num = re.split(house_patt, street_plus_num[1])
            if len(street_and_num) > 1:
                house_num = re.sub(r'(\d+)\s*([абвгдеёжийлмнпрстуфхцчшщъыьэюя]+)',
                                   lambda pat: pat.group(1) + pat.group(2).upper(), street_and_num[1]).replace(' ', '')
                poi = dict(Label=str(house_num), HouseNumber=str(house_num), Data0=data0,
                           StreetDesc=str(prefix + street_and_num[0] + postfix), Type='0x1916')
            else:
                poi = dict(Label=street_plus_num[1], Type='0x1a00', Data0=data0)
        else:
            poi = dict(Label=address, Type='0x1a00', Data0=data0)
    except Exception as e:
        print(e)
        return False

    return poi


def write_poi(poi, file):
    file.write('[POI]\n')

    for key, val in poi.items():
        file.write(f'{key}={val}\n')

    file.write('[END]\n\n')
