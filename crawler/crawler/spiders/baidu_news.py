# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request


class PttSpider(scrapy.Spider):

    name = 'baiduNews'

    def start_requests(self):
        url = 'http://news.baidu.com'
        request = Request(url, callback=self.parse_title)
        yield request

    def parse_title(self, response):
        hotnews_list = response.xpath('//*[@id="pane-news"]/div/ul/li/strong/a/text()').extract()
        url_list = response.xpath('//*[@id="pane-news"]/div/ul/li/strong/a/@href').extract()
        for url in url_list:
            yield Request(url)

    def parse(self, response):
        print(response.xpath('//div[@class="subject"]').extract())
