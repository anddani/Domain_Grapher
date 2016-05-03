# Scrapy
import config
from scrapy.crawler import CrawlerProcess

# Custom spider
from scrape.scrape.spiders.MySpider import MySpider


class ScrapySpider:
    def __init__(self):
        spider = MySpider()

        # DEBUG
        print(config.scrapy_name)
        print(str(config.allowed_domains))
        print(str(config.start_urls))

        process = CrawlerProcess()
        process.crawl(spider)
        process.start()
