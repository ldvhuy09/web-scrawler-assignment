
import scrapy

class VnExpressPage(scrapy.Item):
    #title of page
    title = scrapy.Field()

    #fully html of page
    full_html = scrapy.Field()

    #only text of page
    text_page = scrapy.Field()



