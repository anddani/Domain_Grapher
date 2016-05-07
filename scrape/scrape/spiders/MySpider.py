import config
# import tldextract
from urlparse import urlparse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrape.scrape.items import CurrentPage


class MySpider(CrawlSpider):
    name = config.scrapy_name
    allowed_domains = config.allowed_domains
    start_urls = config.start_urls
    custom_settings = config.custom_settings
    # Follow any link
    rules = [
        Rule(LinkExtractor(),
             callback='parse_item',
             follow=True),
    ]

    def parse_item(self, response):
        print response.url

        # Parse link of current page
        url = urlparse(response.url)
        current_page = CurrentPage()
        current_page['domain'] = url.hostname
        current_page['path'] = url.path

        # DEBUG
        print "domain: ", current_page['domain']
        print "path: ", current_page['path']
        # print Selector(response).xpath('//a/@href').extract()

        current_page['found_links'] = {}
        for link in Selector(response).xpath('//a/@href').extract():
            # Skip all anchors
            if not link or link[0] == '#':
                continue

            # Parse the found links on current page
            # link_url = tldextract.extract(link).registered_domain
            # current_url = tldextract.extract(response.url).registered_domain
            link_url = urlparse(link).netloc
            current_url = url.netloc
            if link_url == current_url:
                continue
            elif link_url == '':
                continue
            if link_url not in current_page['found_links']:
                current_page['found_links'][link_url.lower()] = 1
            else:
                current_page['found_links'][link_url.lower()] += 1

        yield current_page
        return
