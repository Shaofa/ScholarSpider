# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    domain = scrapy.Field()
    title = scrapy.Field()
    author  = scrapy.Field()
    date = scrapy.Field()
    mail = scrapy.Field()
    link = scrapy.Field()
    
    index = 0;
    
    def __init__(self):
        scrapy.Item.__init__(self)
        pass
        
    def __str__(self):
        # print "[%d]--------------------------------------------------" %(SpiderItem.index)
        # print "domain: %s" %(self['domain'])
        # print "title:  %s" %(self['title'])
        # print "author: %s" %(self['author'])
        # print "date:   %s" %(self['date'])
        # print "mail:   %s" %(self['mail'])
        # print "link:   %s" %(self['link'])
        # SpiderItem.index += 1
        return ""

    def process_item(self, item, spider):
        pass

