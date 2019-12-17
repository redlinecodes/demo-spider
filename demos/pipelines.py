# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongodbPipeline(object):
    collection_name = "news_articles"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("") # this is the url string for the db
        self.db = self.client["NEWS"] # this is the name of the database

    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
