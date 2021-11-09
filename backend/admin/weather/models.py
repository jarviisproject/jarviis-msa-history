import time

from django.db import models

# Create your models here.
from admin.common.models import ValueObject
from bs4 import BeautifulSoup
from selenium import webdriver


class Weather(object):
    def __init__(self):
        pass

    def process(self):
        vo = ValueObject()
        # self.weather(vo)
        self.search_by_loc(vo)

    def search_by_loc(self, vo):
        vo.context = 'admin/weather/data/'
        vo.url = 'https://www.weather.go.kr/w/index.do#'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver.exe')
        driver.maximize_window()
        driver.get(vo.url)
        time.sleep(3)
        search = driver.find_element_by_class_name('input')
        search.clear()
        search.send_keys("동작구")
        time.sleep(3)
        driver.find_element_by_css_selector("#index-local-search > div.cmp-local-search-items.on.opened.places > ul > li:nth-child(1) > a").click()
        self.crawling(driver)

    def crawling(self, driver):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        weather = soup.find('span', {'class':'wic DB05 large'}).string
        location = soup.find_all('div', {'class':'serch-area accordionsecond-wrap'})
        driver.close()
        print(location)
        print(weather)
