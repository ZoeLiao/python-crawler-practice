# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttItem(scrapy.Item):
    board = scrapy.Field()
    board_url = scrapy.Field()
    board_articles = scrapy.Field()
