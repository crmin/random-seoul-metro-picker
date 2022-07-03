import csv
import os
import sys
from random import SystemRandom

from scrap import scrap_stations

ONLY_SEOUL = True


def read_stations_from_csv():
    stations_csv_path = 'stations.csv'

    # 이전에 실행된 적 없으면 데이터 수집 진행
    if not os.path.exists(stations_csv_path):
        scrap_stations()

    with open(stations_csv_path) as f:
        csv_stations = list(csv.reader(f))
    column_names = ['station', 'station_eng', 'location']

    # list(dict) 형식으로 변환해서 반환
    return [dict(zip(column_names, line)) for line in csv_stations]


def pick_stations(pick_num, only_seoul):
    """
    Args:
        pick_num (int): 뽑을 역 개수
        only_seoul (bool): 서울만 포함하는지 여부
    """
    stations = read_stations_from_csv()

    if only_seoul:
        stations = [each for each in stations if '서울특별시' in each['location']]

    sys_random = SystemRandom()
    sys_random.shuffle(stations)
    picked_stations = stations[:pick_num]
    print('\n'.join([each['station'] for each in picked_stations]))


if __name__ == '__main__':
    pick_num = 1
    if len(sys.argv) == 2:
        try:
            pick_num = int(sys.argv[1])
        except ValueError:  # not number
            pass  # -> default value (=1)

    pick_stations(pick_num, ONLY_SEOUL)
