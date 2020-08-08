import scrapy
from mySpider.items import NewsItem

class HitszSpider(scrapy.Spider):
    name = 'hitsz'
    allowed_domains = ['hitsz.edu.cn']
    start_urls = ['http://www.hitsz.edu.cn/article/\
        id-77.html?maxPageItems=20&keywords=&pager.offset=0']
    offset = 0
    def parse(self, response):
        for each in response.xpath('/html/body/div[2]/div[2]/div/div/ul/li'):
            item = NewsItem()
            item['url'] = 'http://www.hitsz.edu.cn' +\
                each.xpath('div/a/@href').extract()[0]
            item['title'] = each.xpath('div/a/text()').extract()[0].strip()
            item['date'] = each.xpath('div/span[1]/text()').extract()[0]
            yield item
        if self.offset <= 1960:
            self.offset += 20
            next_url = 'http://www.hitsz.edu.cn/article/\
                id-77.html?maxPageItems=20&keywords=&pager.offset='+ \
                    str(self.offset)
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url,callback=self.parse)