import scrapy
from scrapy.utils.response import open_in_browser
import time

from crawer.items import ArticleItem

class nbaSpider(scrapy.Spider):
    name = 'nbaSpider'
    allow_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self,response):
        url = 'https://nba.udn.com/nba/index?gr=www'
        yield scrapy.Request (url, callback=self.get_articles)

    def get_articles(self,response):
        urls = response.css('div#news_body dt a::attr(href)')
        yield scrapy.Request ('https://nba.udn.com'+urls[0].extract(), callback=self.parse_article)   
        yield scrapy.Request ('https://nba.udn.com'+urls[1].extract(), callback=self.parse_article)   
        yield scrapy.Request ('https://nba.udn.com'+urls[2].extract(), callback=self.parse_article)   

    def parse_article(self,response):
        item = ArticleItem()
        target = response.css('div#story_body_content')
        try:
            item['title'] = target.css("h1.story_art_title::text")[0].extract()
            item['content'] = target.css("span p::text").extract()
            item['image_url'] = target.css("span figure.photo_center a img::attr(data-src)")[0].extract()
            item['source_url'] = response.url
            item['publish_time'] = target.css("span::text")[0].extract()
            yield item
        except IndexError:
            raise       