# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/post']
    #启动时调用重写的start_urls 函数，而不是调用默认的start_urls 方法
    def start_requests(self):
        yield scrapy.Request(url='http://httpbin.org/post',method='POST',callback=self.parse_post)

    #默认的start_requests方法调用了 make_requests_from_url
    def make_requests_from_url(self, url):
        return scrapy.Request(url=url,callback=self.parse_post)

    def parse(self, response):
        pass

    def parse_post(self,response):
        print('hello',response.status)