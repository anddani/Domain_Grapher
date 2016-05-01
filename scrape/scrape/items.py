# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CurrentPage(scrapy.Item):
    # define the fields for your item here like:

    # Domain of the current scrape
    domain = scrapy.Field()
    # Specific path of the current scrape
    path = scrapy.Field()
    # Hash with found links and their corresponding frequency
    found_links = scrapy.Field()
    pass
