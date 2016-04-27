import config
import scrapy
from urlparse import urlparse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy.selector import Selector
from scrape.scrape.items import CurrentPage


class MySpider(scrapy.Spider):
    name = config.scrapy_name
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    # Follow any link
    rules = (
        Rule(LinkExtractor(allow=(r'/.*', )), callback='parse'),
    )

    def parse(self, response):
        print response.url
        url = urlparse(response.url)
        current_page = CurrentPage()
        current_page['domain'] = url.hostname
        current_page['page'] = url.page
        for link in Selector(response).xpath('//a/@href').extract():
            link_url = urlparse(link)
            if link_url.hostname in current_page['found_links']:
                current_page['found_links'][link_url.hostname] += 1
            else:
                current_page['found_links'][link_url.hostname] = 1
            print link
        yield current_page
        return
        # print 'Selector: ', str(Selector(response))
        # return Selector(response).xpath('//a').extract()
