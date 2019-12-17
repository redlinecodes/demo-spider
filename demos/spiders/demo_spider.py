# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DemoSpiderSpider(CrawlSpider):
    name = 'demo_spider'
    allowed_domains = ['motortrend.com']
    # start_urls = ['http://motortrend.com/']

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36 (Acebot/0.1)'

    def start_requests(self):
        yield scrapy.Request(url='https://www.motortrend.com/auto-news/', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//article//div//a[2]"), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='load-more-button button']"), process_request='set_user_agent')
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        {
            'title': response.xpath("normalize-space(//h1[@class='NNlNP'])").get(),
            'author': response.xpath("normalize-space(//a[@class='_2oExj']/text())").get(),
            'date': response.xpath("normalize-space(//article[1]/section[2]/div[1]/time[1])").get(),
            'p1': response.xpath("normalize-space(//article[1]//section[2]//section[1]//div[4]//p[1])").get(),
            'article': response.xpath("//article[1]/section[2]/section[1]//div//p/text()").getall(),
            'article_url': response.url
        }
