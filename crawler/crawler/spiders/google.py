# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from crawler.items import PttItem


BASE_URL = "https://news.google.com/{}"

class PttSpider(scrapy.Spider):

    name = "google"

    def start_requests(self):
        url = BASE_URL.format('?hl=zh-TW&gl=TW&ceid=TW:zh-Hant')
        url = BASE_URL
        yield scrapy.Request(url)

    def parse(self, response):
        #items = GoogleItem()
        articles = response.xpath("//article")
        urls = response.xpath("//article/a/@href").extract()
        title = response.xpath("//article/h3/a/text()").extract()
        source = response.xpath("//article/div/div/a/text()").extract()
        time = response.xpath("//article/div/div/time/@datetime").extract()
        print('title:', title[0])
        print('source:', source[0])
        print('time:', time[0])
        print('url:', urls[0])
        #for a in articles: 
        #    urls = a.xpath("./a/@href").extract()
        #    title = a.xpath("./h3/a/text()").extract()
        #    source = a.xpath("./div/div/a/text()").extract()
        #    time = a.xpath("./div/div/time/@datetime").extract()
        #    print('title:', title[0])
        #    print('source:', source[0])
        #    print('time:', time[0])
        #    print('url:', urls[0])
