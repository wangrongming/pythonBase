# -*- coding: utf-8 -*-
from scrapy import Spider,FormRequest,Request
import re
from weibosearch.items import WeibosearchItem


class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    start_urls = ['http://weibo.cn/']

    search_url='https://weibo.cn/search/mblog'
    max_page = 100

    def start_requests(self):
        keyword='00001'
        url = '{url}?keyword1={keyword}'.format(url=self.search_url,keyword=keyword)
        for page in range(self.max_page+1):
            data = {
                'mp':str(self.max_page),
                'page':str(4),
            }
        yield FormRequest(url,callback=self.parse_index,formdata=data)

    def parse_index(self, response):
        weibos = response.xpath('//div[@class="c" and contains(@id,"M_")]')
        for weibo in weibos:
            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').extract_first())
            if is_forward:
                detail_url = weibo.xpath('.//a[contains(.,"原文评论[")]//@href').extract_first()
                #包含原文评论的 是超链接
            else:
                detail_url = weibo.xpath('(.//a[contains(.,"评论[")]/@href)').extract_first()
            yield Request(detail_url,callback=self.parse_detail,meta={'keyword':response.meta.get('keyword')})

    def parse_detail(self, response):
        url = response.url
        content = ''.join(response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract())
        id = re.search('comment\/(.*?)\?', response.url).group(1)
        comment_count = response.xpath('//span[@class="pms"]//text()').re_first('评论\[(.*?)\]')
        forward_count = response.xpath('//a[contains(., "转发[")]//text()').re_first('转发\[(.*?)\]')
        like_count = response.xpath('//a[contains(., "赞[")]//text()').re_first('赞\[(.*?)\]')
        posted_at = response.xpath('//div[@id="M_"]//span[@class="ct"]//text()').extract_first(default=None)
        user = response.xpath('//div[@id="M_"]/div[1]/a/text()').extract_first()
        keyword = response.meta.get('keyword')
        weibo_item = WeibosearchItem()
        for field in weibo_item.fields:
            try:
                weibo_item[field] = eval(field)
            except NameError:
                print('Field is Not Defined', field)
        yield weibo_item