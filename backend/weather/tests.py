from datetime import datetime

import requests
from django.test import TestCase

# Create your tests here.


class Weather(object):
    def __init__(self):
        pass

    def api_test(self):
        # 강남구 위경도
        nx = 61
        ny = 126
        # 현재 시간
        now = datetime.now()
        base_date = f'{now.year}{now.month if now.month>9 else f"0{now.month}"}{now.day if now.day>9 else f"0{now.day}"}'
        # 1일 총 8번 데이터가 업데이트 된다.(0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300)
        # 현재 api를 가져오려는 시점의 이전 시각에 업데이트된 데이터를 base_time, base_date로 설정
        if now.hour < 2 or (now.hour == 2 and now.minute <= 10):  # 0시~2시 10분 사이
            base_time = "2300"
        elif now.hour < 5 or (now.hour == 5 and now.minute <= 10):  # 2시 11분~5시 10분 사이
            base_time = "0200"
        elif now.hour < 8 or (now.hour == 8 and now.minute <= 10):  # 5시 11분~8시 10분 사이
            base_time = "0500"
        elif now.hour <= 11 or now.minute <= 10:  # 8시 11분~11시 10분 사이
            base_time = "0800"
        elif now.hour < 14 or (now.hour == 14 and now.minute <= 10):  # 11시 11분~14시 10분 사이
            base_time = "1100"
        elif now.hour < 17 or (now.hour == 17 and now.minute <= 10):  # 14시 11분~17시 10분 사이
            base_time = "1400"
        elif now.hour < 20 or (now.hour == 20 and now.minute <= 10):  # 17시 11분~20시 10분 사이
            base_time = "1700"
        elif now.hour < 23 or (now.hour == 23 and now.minute <= 10):  # 20시 11분~23시 10분 사이
            base_time = "2000"
        else:  # 23시 11분~23시 59분
            base_time = "2300"
        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
        params = {'serviceKey': 'Azs8t5lc5MVlv67BnCCXpwjGc9eLdowYV2q3MZO0wqwOkWo3vpUP0PsHimKL0osXusxlIb+888C2E+PquYdixQ==',
                  'pageNo': '1',
                  'numOfRows': '10',
                  'dataType': 'JSON',
                  'base_date': base_date,
                  'base_time': base_time,
                  'nx': f'{nx}',
                  'ny': f'{ny}'}
        response = requests.get(url, params=params)
        weather = response.json().get('response').get('body').get('items')
        weather = list(weather.values())[0]
        '''
        - 하늘상태(SKY) 코드 : 맑음(1), 구름많음(3), 흐림(4)
        - 강수형태(PTY) 코드 : (단기) 없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4) 
        '''
        for i in weather:
            if i['category'] == 'SKY':
                sky = i
            elif i['category'] == 'PTY':
                pty = i
        print(f'SKY : {sky}')
        print(f'PTY : {pty}')


if __name__ == '__main__':
    w = Weather()
    w.api_test()