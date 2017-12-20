# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名
    movie_title = Field()
    # 导演
    movie_director = Field()
    # 主演
    movie_actors = Field()
    # 评分
    movie_rate = Field()
    # 地点
    movie_region = Field()
    # 上映时间
    movie_date = Field()
    # 时长
    movie_duration = Field()
    # 描述
    movie_ticket = Field()
    pass












