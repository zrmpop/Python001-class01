# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        # output = f'{title} link: {link}\r\n'
        # with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as movie:
        #     movie.write(output)
        # return item

        output = [f'{title} link: {link}']
        movie = pd.DataFrame(data=output)
        movie.to_csv('./movieList2.csv', mode='a', encoding='utf8',
                     index=False, header=False)
