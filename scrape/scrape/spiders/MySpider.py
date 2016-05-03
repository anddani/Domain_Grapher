import config
import tldextract
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
    # rules = [
    #     Rule(LinkExtractor(allow=('/r/pics/\?count=\d*&after=\w*', )),
    #          callback='parse_item',
    #          follow=True),
    # ]
    rules = [
        Rule(LinkExtractor(allow=('/r/pics/\?count=\d*&after=\w*', )),
             callback='parse_item')
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
            if link[0] == '#':
                continue

            # DEBUG
            # print "Parsing: ", link

            # Parse the found links on current page
            link_url = tldextract.extract(link)
            if link_url.registered_domain not in current_page['found_links']:
                current_page['found_links'][link_url.registered_domain] = 1
            else:
                current_page['found_links'][link_url.registered_domain] += 1

        yield current_page
        return
        # print 'Selector: ', str(Selector(response))
        # return Selector(response).xpath('//a').extract()
