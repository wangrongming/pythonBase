# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class WeibosearchItem(scrapy.Item):
    table_name = 'weibo'

    id = Field()
    content = Field()
    forward_count = Field()
    comment_count = Field()
    like_count = Field()
    posted_at = Field()
    url = Field()
    user = Field()
    keyword = Field()
    crawled_at = Field()
