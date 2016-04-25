import config
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.selector import Selector


class MySpider(scrapy.Spider):
    name = config.scrapy_name
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    rules = (
        Rule(LinkExtractor(allow=(r'<a.*', )), callback='parse'),
    )

    def parse(self, response):
        print response.url
        for link in Selector(response).xpath('//a').extract():
            print link
        # print 'Selector: ', str(Selector(response))
        # return Selector(response).xpath('//a').extract()
