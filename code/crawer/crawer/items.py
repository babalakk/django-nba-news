# -*- coding: utf-8 -*-
import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    image_url = scrapy.Field()
    source_url = scrapy.Field()
    publish_time = scrapy.Field()