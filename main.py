from datetime import datetime
from sys import argv
from time import sleep
from json.decoder import JSONDecodeError

import requests

import POI
import constants
from funcs import parse_address, write_poi


def parse(c, num):
    global REQUESTS_NUM

    while True:
        REQUESTS_NUM += 1

        try:
            resp = session.get(LINK.format(num=num, lat=c[0], lon=c[1]))
            sleep(3)
            return resp
        except requests.ConnectionError:
            pass

        print('Обрыв соединения, повторная попытка подключения через 0.2с')
        sleep(3)


def main(f_name):
    f_name = input('Введите имя файла: ') if not f_name else f_name
    pois = POI.get_cds(f_name)
    f_out_name = ''.join(f_name.split('.')[:-1]) + '-out.' + f_name.split('.')[-1]

    f_out = open(f_out_name, 'w')

    f_out.write(constants.header)

    for counter, poi in enumerate(pois, 1):

        print()

        try:
            data = parse(poi, 5).json()
            print(f'POI number (UCH) - {counter} / {len(pois)}')
            try:
                poi_data = parse_address(data['features'][0]['attrs']['address'], f'({poi[0]},{poi[1]})')
                print(f'Адрес для {poi[0]}, {poi[1]} найден (OKS)')
                write_poi(poi_data, f_out)
            except IndexError:
                data = parse(poi, 1).json()
                print(f'Адрес для {poi[0]}, {poi[1]} не найден (OKS), поиск по участку...')
                try:
                    poi_data = parse_address(data['features'][0]['attrs']['address'], f'({poi[0]},{poi[1]})')
                    print(f'Адрес для {poi[0]}, {poi[1]} найден (UCH)')
                    write_poi(poi_data, f_out)
                except IndexError:
                    print(f'Адрес для {poi[0]}, {poi[1]} не найден (UCH)')
                    write_poi(dict(Type='0x1a00', Data0=f'({poi[0]},{poi[1]})'), f_out)
        except JSONDecodeError:
            with open('log.html', 'wb') as file:
                file.write(parse(poi, 5).content)
            with open('log.txt', 'w', encoding='utf-8') as file:
                file.write(f'Обработано точек - {counter}')

            exit(1)

    f_out.flush()
    f_out.close()


if __name__ == '__main__':
    START = datetime.now()
    REQUESTS_NUM = 0
    LINK = 'https://pkk.rosreestr.ru/api/features/{num}?text={lat}+{lon}'

    session = requests.Session()

    # proxy = 'socks5://84GAJv:APZgSw@193.31.102.18:9212/'
    proxy = 'https://84GAJv:APZgSw@193.31.102.18:9212/'

    # session.proxies = {
    #     'https': proxy
    # }

    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 '
                      'YaBrowser/20.7.1.68 Yowser/2.5 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'pkk.rosreestr.ru',
        'Referer': 'https://pkk.rosreestr.ru/'
    }

    attr = argv[1] if argv[1:] else ''

    try:
        main(attr)
    except Exception as e:
        with open('log.txt', 'a') as error_log:
            error_log.write(str(e))

    print('Время выполнения:', datetime.now() - START)
    print(f'Кол-во запросов: {REQUESTS_NUM}')
