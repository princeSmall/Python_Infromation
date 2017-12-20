# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector
from Movie.items import MovieItem


class DoubanSpider(Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com"]

    def parse(self,response):
        items = []
        sel = Selector(response)
        sites = sel.xpath('//div[@id="screening"]/div[@class="screening-bd"]/ul/li')
        for site in sites:
            item = MovieItem()
            item['movie_title'] = site.xpath('@data-title').extract()
            item['movie_director'] = site.xpath('@data-director').extract()
            item['movie_actors'] = site.xpath('@data-actors').extract()
            item['movie_rate'] = site.xpath('@data-rate').extract()
            item['movie_region'] = site.xpath('@data-region').extract()
            item['movie_date'] = site.xpath('@data-release').extract()
            item['movie_duration'] = site.xpath('@data-duration').extract()
            item['movie_ticket'] = site.xpath('@data-ticket').extract()
            items.append(item)
        print items, '.....'
        return items

