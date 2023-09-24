# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class DevilfruitscrapePipeline:

    collection_name = 'devilfruits'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # Get uri and db from settings.py
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'),
                   mongo_db=crawler.settings.get('MONGO_DATABASE', 'items'))

    def open_spider(self, spider):
        # Connect to cluster
        self.cluster = pymongo.MongoClient(self.mongo_uri, ssl=True)

        # Get database
        self.db = self.cluster[self.mongo_db]

        # Delete every item in collection
        self.db[self.collection_name].delete_many({})

    def close_spider(self, spider):
        self.cluster.close()

    def store_item(self, item):

        item['info'] = item['info'].replace('"', '\\"')

        self.db[self.collection_name].insert_one(dict(item))

    def process_item(self, item, spider):
        self.store_item(item)
        return item
