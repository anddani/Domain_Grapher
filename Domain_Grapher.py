#!/usr/bin/env python
from Scrapy_Spider import ScrapySpider
import config
import re
import tldextract
from urllib2 import urlopen

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
            return False;
        else:
            config.allowed_domains[0] = tldextract.extract(domain_name).registered_domain
            config.start_urls[0] = domain_name
            return True;
    except:
        return False

while True:
    # Header
    print '=============================='
    print '=       Domain Grapher       ='
    print '= -------------------------- ='
    print '=                version 0.1 ='

    # Menu
    print '=============================='
    print '=                            ='
    print '=  1. Change Domain          ='
    print '=  2. Start Crawl            ='
    print '=  3. Drop Tables            ='
    print '=  0. Exit                   ='
    print '=                            ='
    print '=============================='
    print 'Current domain: ' + config.allowed_domains[0]
    print 'Current url formatted for scrapy: ' + config.start_urls[0]

    item = raw_input('Choose between [0-3]: ')

    if item == '1':
        domain_name = raw_input('Change domain...\n')
        if not valid_url(domain_name):
            print '"' + domain_name + '"' + ' is an invalid domain'
    elif item == '2':
        print('Starting Crawl...')
        ss = ScrapySpider()
        break
    elif item == '3':
        print('Dropping all tables...')
    elif item == '0':
        print('Exiting...')
        break
    else:
        print('Invalid input.')
