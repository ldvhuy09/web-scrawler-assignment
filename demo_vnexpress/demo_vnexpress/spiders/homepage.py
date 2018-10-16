import scrapy

class HomePageSpider(scrapy.Spider):
    #mỗi spider sẽ có một tên
    name = 'homepage_spider'

    def start_requests(self):
        #Cần trả về scrapy.Request 
        #để spider gửi request đúng
        url = 'https://vnexpress.net/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): 
        #sau khi thực hiện request, scrapy sẽ nhận được response
        #sau đó gọi callback function -> self.parse để thực hiện
        #parse response
        f = open('result.txt', 'w')
        #newses = response.xpath('//div[@class="sub_featured"]').extract()
        #newses =  response.xpath('//div[contains(@class, "sub_featured")]/ul/li/a/text()').extract()
        newses = response.xpath('//body//text()').extract()
        print(newses)
        for news in newses:
            f.write(news) 
        f.close()
