# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DevilfruitscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    fruit_type = scrapy.Field()
    price = scrapy.Field()
    imagelink = scrapy.Field()
    english_name = scrapy.Field()
    meaning = scrapy.Field()
    info = scrapy.Field()
