from django.test import TestCase

# Create your tests here.
import json

from django.test import TestCase
from sphinx.util import requests


def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    headers = {"Authorization": "KakaoAK 851f4e6cf0cce36ebf456a4eb33b94d4"}
    # get 방식으로 주소를 포함한 링크를 헤더와 넘기면 result에 json형식의 주소와 위도경도 내용들이 출력된다.
    result = json.loads(str(requests.get(url, headers=headers).text))
    status_code = requests.get(url, headers=headers).status_code
    if (status_code != 200):
        # print(f"ERROR: Unable to call rest api, http_status_coe: {status_code}")
        return 0

    # print(requests.get(url, headers=headers))
    # print(result)

    try:
        match_first = result['documents'][0]['address']
        lon = match_first['x']
        lat = match_first['y']
        # print(lon, lat)
        print(match_first)

        return lon, lat
    except IndexError:  # match값이 없을때
        return print('match값이 없을때')
    except TypeError:  # match값이 2개이상일때
        return print('match값이 2개이상일때')


def getAddress(keyword):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + keyword
    headers = {"Authorization": "KakaoAK 851f4e6cf0cce36ebf456a4eb33b94d4"}
    # get 방식으로 주소를 포함한 링크를 헤더와 넘기면 result에 json형식의 주소와 위도경도 내용들이 출력된다.
    result = json.loads(str(requests.get(url, headers=headers).text))
    status_code = requests.get(url, headers=headers).status_code
    if (status_code != 200):
        # print(f"ERROR: Unable to call rest api, http_status_coe: {status_code}")
        return 0

    print(requests.get(url, headers=headers))
    print(result)

    try:
        match_first = result['documents'][0]
        x = match_first['x']
        y = match_first['y']
        address = match_first['road_address_name']
        print(x)
        print(y)
        print(address)

        return x, y, address
    except IndexError:  # match값이 없을때
        return print('match값이 없을때')
    except TypeError:  # match값이 2개이상일때
        return print('match값이 2개이상일때')


if __name__ == '__main__':
    # getLatLng('서울특별시 서초구 강남대로 373 홍우빌딩 1층')
    getAddress('더달달 카페')