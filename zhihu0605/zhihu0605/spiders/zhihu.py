# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import json
from zhihu0605.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']

    start_user = 'qian-li-20-12'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include{include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include{include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user,include=self.user_query),self.user_parse)
        # yield Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),

        #               self.follows_parse)


    def user_parse(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(
            self.follows_url.format(user=result.get('url_token'),include=self.follows_query,limit=20,offset=0),
            self.follows_parse
        )

    def follows_parse(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.user_parse)

        # if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
        #     next_page = results.get('paging').get('next')
        #     yield Request(next_page,
        #                   self.follows_parse)

