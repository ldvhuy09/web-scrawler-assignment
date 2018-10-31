# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider


class CrawlVnexpressSpider(scrapy.Spider):
    name = 'crawl_vnexpress'
    allowed_domains = ['vnexpress.vn']
    
    custom_settings = {
        'DEPTH_LIMIT': 7,
        'CONCURRENT_REQUESTS': 200,
        'LOG_LEVEL': 'INFO',
        'COOKIES_ENABLED': False
    }
    
    # rules = [
    #     Rule(
    #         LinkExtractor(
    #             canonicalize=True,
    #             unique=True
    #         ),
    #         follow=True,
    #         callback="parse_items"
    #     )
    # ]

    def start_requests(self):
        url = 'http://vnexpress.vn/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//head/title/text()').extract()[0]

        file_text = open('{}.txt'.format(title), 'w')
        file_html = open('{}.html'.format(title), 'wb')
        except_script_tag = '*[not(self::script)]'
        text_in_page = response.xpath('//*[not(self::script) and string-length(text()) > 0]/text()').extract()
        for text in text_in_page:
            if (not text.isspace()):
                file_text.write(text)

        file_html.write(response.body)

        file_text.close()
        file_html.close()
        
        
