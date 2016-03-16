# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ScholarPipeline(object):

    def __init__(self):
        self.file = None

    def open_spider(self,spider):
        if self.file is not None:
            self.file.close()
        self.file = open("data_%s.jl" % spider.name, 'wb')

    def close_spider(self, spider):
        if self.file is not None:
            self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        print line
        return item
