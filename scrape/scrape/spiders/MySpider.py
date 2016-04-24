import os
import inspect
import config
import sys
from scrapy.spider import Spider
from scrapy.selector import Selector

# Get paths
abspath = os.path.abspath(inspect.getfile(inspect.currentframe))
currentdir = os.path.dirname(abspath)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class MySpider(Spider):
    name = config.scrapy_name
    allowed_domains = config.domain_list
    start_urls = config.start_urls

    def parse(self, response):
        return Selector(response).xpath('//a').extract()
