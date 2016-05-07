#!/usr/bin/env python
import config
import re
# import tldextract
from urlparse import urlparse
from py2neo import Graph
from py2neo import authenticate
from urllib2 import urlopen
from Scrapy_Spider import ScrapySpider


def valid_url(domain_name):
    try:
        if not re.match('^https?://*', domain_name):
            domain_name = 'http://' + domain_name
        code = urlopen(domain_name).code
        # Status codes
        # 2xx - successful
        # 3xx - forwarding
        # >=4xx - error
        if code / 100 >= 4:
            return False
        else:
            # reg_domain = tldextract.extract(domain_name).registered_domain
            reg_domain = urlparse(domain_name).netloc
            print reg_domain
            config.allowed_domains[0] = reg_domain
            config.start_urls[0] = domain_name
            return True
    except:
        return False

while True:
    # Header
    print '=============================='
    print '=       Domain Grapher       ='
    print '= -------------------------- ='
    print '=                version 0.5 ='

    # Menu
    print '=============================='
    print '=                            ='
    print '=  1. Change Domain          ='
    print '=  2. Start Crawl            ='
    print '=  3. Drop Rows              ='
    print '=  0. Exit                   ='
    print '=                            ='
    print '=============================='
    print 'Current domain: ' + config.allowed_domains[0]
    print 'Current url formatted for scrapy: ' + config.start_urls[0]

    item = raw_input('Choose between [0-3]: ')

    if item == '1':
        domain_name = raw_input('Please enter the new domain: ')
        if not valid_url(domain_name):
            print '"' + domain_name + '"' + ' is an invalid domain'
    elif item == '2':
        print 'Starting Crawl...'
        ss = ScrapySpider()
        break
    elif item == '3':
        print 'Dropping all rows...'
        authenticate(config.NEO4J_HOST,
                     config.NEO4J_USER,
                     config.NEO4J_PASSWORD)
        graph = Graph(config.NEO4J_DATA_URL)
        graph.cypher.execute("MATCH (n) DETACH DELETE n")
        print 'ROWS HAVE BEEN DELETED SUCCESSFULLY'
    elif item == '0':
        print 'Exiting...'
        break
    else:
        print 'Invalid input.'
