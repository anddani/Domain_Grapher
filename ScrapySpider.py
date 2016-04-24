# Scrapy
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import config
# from scrapy.utils.project import get_project_settings

# Custom spider
from .scrape.scrape.spiders import MySpider


class ScrapySpider(MySpider):
    def __init__(self, arg):
        dispatcher.connect(reactor.stop, signals.spider_closed)
        spider = MySpider()
        crawler = Crawler(Settings())
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()

        print(config.scrapy_name)
        print(str(config.allowed_domains))
        print(str(config.start_urls))

        reactor.run()
        self.show_output()

    def show_output():
        for web_num in range(len(config.total_products_list)):
            website = config.total_products_list[web_num]
            print(website[config.init_num].get('web'))
