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
        atags = Selector(response=response).xpath(
            '//dd/div/a[@data-act="movies-click"]')

        # print(len(atags))
        print(atags)
        for atag in atags:
            if counter <= 10:
                title = atag.xpath('./text()').extract_first()
                link = 'https://maoyan.com' + \
                    atag.xpath('./@href').extract_first()
                item = MaoyanmovieItem()
                item['title'] = title
                item['link'] = link
                counter += 1
                yield item
            else:
                yield
