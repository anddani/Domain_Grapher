NEO4J_HOST = 'localhost:7474'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'DD2471'
NEO4J_DATA_URL = 'http://' + NEO4J_HOST + '/db/data'

scrapy_name = 'somespider'
allowed_domains = ['reddit.com']
start_urls = [
    'https://www.reddit.com/r/pics',
]
custom_settings = {
    "ITEM_PIPELINES": {
        'scrape.scrape.pipelines.CurrentPagePipeline': 300,
    }
}
# allowed_domains = ['dustyfeet.com']
# start_urls = [
#     'http://www.dustyfeet.com/',
# ]
