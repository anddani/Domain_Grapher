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
        print item['domain'], item['path'], ' ', str(item['found_links'])

        # merge_one ensure uniqueness of entities
        currentDomain = self.graph.merge_one("Page", "domain", item['domain'])
        # currentDomain.properties['name'] = item['domain']
        # currentDomain.push()
        for link in item['found_links']:
            link_node = self.graph.merge_one('Link', 'id', link)
            # link_node.properties['name'] = item['found_links'][link]
            # link_node['name']
            # link_node.push()
            self.graph.create_unique(Relationship(currentDomain, 'LINKS TO', link_node))
        return item
