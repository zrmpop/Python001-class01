# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=1']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&sortId=1'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        counter = 0
        divTags = Selector(response=response).xpath(
            '//dd/div/div[@class="movie-item-hover"]')

        for divTag in divTags:
            if counter <= 10:
                title = divTag.xpath(
                    './a/div/div/span[@class="name "]/text()').extract_first()
                link = divTag.xpath(
                    './a[@data-act="movie-click"]/@href').extract_first()
                cat = divTag.xpath(
                    './a/div/div[2]/text()').extract()[1].strip('\n').strip()
                time = divTag.xpath(
                    './a/div/div[4]/text()').extract()[1].strip('\n').strip()

                item = MaoyanmovieItem()
                item['title'] = title
                item['link'] = 'https://maoyan.com' + link
                item['time'] = time
                item['category'] = cat
                counter += 1
                yield item
            else:
                yield
