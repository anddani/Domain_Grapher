# -*- coding: utf-8 -*-
import config
from py2neo import Graph
from py2neo import authenticate
from py2neo import Node
from py2neo import Relationship


class CurrentPagePipeline(object):
    print 'Starting connection to database'
    authenticate(config.NEO4J_HOST, config.NEO4J_USER, config.NEO4J_PASSWORD)
    graph = Graph(config.NEO4J_DATA_URL)

    def process_item(self, item, spider):
        print 'Inserting page: ', item['domain'], item['path']
        return item
