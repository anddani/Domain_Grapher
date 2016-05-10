NEO4J_HOST = 'localhost:7474'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'DD2471'  # Very secret password
NEO4J_DATA_URL = 'http://' + NEO4J_HOST + '/db/data'

scrapy_name = 'somespider'
allowed_domains = ['']
start_urls = [
    '',
]
custom_settings = {
    "ITEM_PIPELINES": {
        'scrape.scrape.pipelines.CurrentPagePipeline': 300,
    }
}
