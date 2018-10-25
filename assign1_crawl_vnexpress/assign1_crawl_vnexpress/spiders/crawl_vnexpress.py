# -*- coding: utf-8 -*-
import scrapy


class CrawlVnexpressSpider(scrapy.Spider):
    name = 'crawl_vnexpress'
    allowed_domains = ['vnexpress.net']
    start_urls = ['http://vnexpress.net/']

    def parse(self, response):
        pass
