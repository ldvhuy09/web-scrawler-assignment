import scrapy

class VnExpressScraperItem(scrapy.Item):
    url_from = scrapy.Field()
    url_to = scrapy.Field()