# -*- coding: utf-8 -*-
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
