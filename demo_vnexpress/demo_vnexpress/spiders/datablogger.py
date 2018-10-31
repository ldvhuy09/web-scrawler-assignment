# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from demo_vnexpress.items import DatabloggerScraperItem

store_folder_default = './resutl/'

class DatabloggerSpider(CrawlSpider):
    # The name of the spider
    name = "datablogger"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["vnexpress.net", "vnexpress.vn"]

    # The URLs to start with
    start_urls = ["https://vnexpress.net/"]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    custom_settings = {
        'DEPTH_LIMIT': 7,
        'CONCURRENT_REQUESTS': 200,
        'LOG_LEVEL': 'INFO',
        'COOKIES_ENABLED': False
    }

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_text(self, title, texts):
        file = open('{}.txt'.format(title), 'w')
        for text in texts:
            if (not text.isspace()):
                file.write(text)
        file.close()

    def parse_html(self, title, body):
        file = open('{}.html'.format(title), 'wb')
        file.write(body)
        file.close()

    # Method for parsing items
    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(allow_domains=self.allowed_domains,canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            
            for allow_domain in self.allowed_domains:
                if allow_domain in link.url:
                    is_allowed = True

            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = DatabloggerScraperItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
            # if is_allowed:
            #     title = response.xpath('//head/title/text()').extract()[0]

            #     texts = response.xpath('//*[not(self::script) and string-length(text()) > 0]/text()').extract()
            #     self.parse_text(title, texts)

            #     self.parse_html(title, response.body)
        return items