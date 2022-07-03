import csv
from pprint import pprint

import requests
from bs4 import BeautifulSoup

uri = 'https://ko.wikipedia.org/wiki/수도권_전철역_목록'

headers = {
    'User-Agent': (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    ),
}


def parse_from_table(table_soup):
    stations = []
    column_names = ('station', 'station_eng', 'location', '_')
    for tr in table_soup.find_all('tr')[1:]:  # 0 -> table column header
        tds = [each.text for each in tr.find_all('td')]
        if len(tds) < 4:  # rowspan으로 합쳐진 table 제외
            continue
        station = dict(zip(column_names, tds))
        del station['_']
        stations.append(station)
    return stations


def get_table_from_page(soup):
    return soup.find_all('table', class_='wikitable')


def save_data_as_csv(stations):
    with open('./stations.csv', 'w') as f:
        transformed_stations = [
            (each['station'], each['station_eng'], each['location']) for each in stations
        ]
        writer = csv.writer(f)
        writer.writerows(transformed_stations)


def scrap_stations():
    resp = requests.get(uri, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    stations = []
    for table in get_table_from_page(soup):
        stations.extend(parse_from_table(table))
    save_data_as_csv(stations)


if __name__ == '__main__':
    scrap_stations()
