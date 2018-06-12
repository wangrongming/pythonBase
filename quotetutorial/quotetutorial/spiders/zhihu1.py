# -*- coding: utf-8 -*-
import scrapy


class Zhihu1Spider(scrapy.Spider):
    name = 'zhihu1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def make_requests_from_url(self, url):
        return scrapy.Request(url=url, meta={'download_timeout':10},callback=self.parse)

    def parse(self, response):
        pass
