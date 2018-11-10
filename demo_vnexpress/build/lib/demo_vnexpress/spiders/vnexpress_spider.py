# -*- coding: utf-8 -*-
import scrapy
from ..constants import *
from ..fileutils import *
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class VnExpressSpider(CrawlSpider):

    name = "vnexpress_crawler"

    allowed_domains = ["vnexpress.net"]

    start_urls = ["https://vnexpress.net/"]

    rules = [
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    custom_settings = CUSTOM_SETTING

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self, response):
        try:
            title = response.xpath('//head/title/text()').extract()[0]
            title.replace('\/', '-')

            texts = response.xpath('//*[not(self::script) and string-length(text()) > 0]/text()').extract()
            self.parse_text(title, texts)

            self.parse_html(title, response.body)
            pass
        except:
            print('Can\'t not extract this page')

        pass

    def parse_text(self, title, texts):
        file = create_file_to_write(FOLDER_RESULT_DEFAULT, title + '.txt')
        for text in texts:
            if (not text.isspace()):
                file.write(text)
        file.close()

    def parse_html(self, title, body):
        file = create_file_to_write(FOLDER_RESULT_DEFAULT, title + '.html', mode='wb')
        file.write(body)
        file.close()