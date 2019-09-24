# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from crawler.items import PttItem


BASE_URL = "https://www.ptt.cc{}"

class PttSpider(scrapy.Spider):

    name = "ptt"

    def start_requests(self):
        url = BASE_URL.format("/bbs/index.html")
        yield scrapy.Request(url, callback=self.parse_urls)

    def parse_urls(self, response):
        urls = response.xpath("//a[@class='board']")
        for i in range(2):
            print('url', urls[i].xpath("./@href").extract()[0])
            url = BASE_URL.format(urls[i].xpath("./@href").extract()[0])
            url_text = urls[i].xpath("./text()").extract()[0]
            yield scrapy.Request(url, meta={"board": url_text})

    def parse(self, response):
        items = PttItem()
        items["board"] = response.meta["board"]
        items["board_url"] = response.url
        items["board_articles"] = {}
        articles = response.xpath("//div[@class='title']")
        for article in articles:
            # TODO: Fix
            url = article.xpath("./@href").extract()[0]
            url_text = article.xpath("./text()").extract()[0] 
            items["board_articles"][url_text] = url
