# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# System imports
import arrow
import pymongo
import ujson

# Scrapy imports
from scrapy.conf import settings
from scrapy.exceptions import DropItem

# Search imports
from crawler.items import *
from crawler.logger import logger
from utils.mongo import (
    baidu_db,
    ptt_db,
)
from models.baidu import Baidu
from models.ptt import Ptt

# url, title, description, date, category, views

class CrawlerPipelinePTT(object):

    def process_item(self, item, spider):
        if isinstance(item, PttItem):
            url = item['url']
            ptt = Ptt.get_by({'url': url})
            now = arrow.utcmow.datetime()
            if ptt:
                item['updated_at'] = now
                result = ptt.update(item)
                if result:
                    logger.info('Update ptt successfully.')
                else:
                    logger.info('Falied to update ptt.')
            else:
                item['created_at'] = now
                result = ptt.create(item)
                if result:
                    logger.info('Insert ptt successfully.')
                else:
                    logger.info('Falied to insert ptt.')
        return item


class CrawlerPipelineBaidu(object):

    def process_item(self, item, spider):
        if isinstance(item, BaiduItem):
            article_id = item['_id']
            baidu = Baidu.get_by({'article_id': article_id})
            now = arrow.utcmow.datetime()
            if baidu:
                item['updated_at'] = now
                result = baidu.update(item)
                if result:
                    logger.info('Update baidu successfully.')
                else:
                    logger.info('Falied to update baidu.')
            else:
                item['created_at'] = now
                result = baidu.create(item)
                if result:
                    logger.info('Insert baidu successfully.')
                else:
                    logger.info('Falied to insert baidu.')
        return item
