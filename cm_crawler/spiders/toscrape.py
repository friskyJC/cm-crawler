# -*- coding: utf-8 -*-
import scrapy

from cm_crawler.common import utility
from cm_crawler.items import ToscrapeItem

class ToscrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item = ToscrapeItem()
            item['text'] = quote.xpath(
                './span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath(
                './/small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath(
                './/div[@class="tags"]/a[@class="tag"]/text()').extract()
            item['token'] = utility.gen_md5_token(item['text'])
            yield item

        # for quote in response.css("div.quote"):
        #     yield {
        #         'text': quote.css("span.text::text").extract_first(),
        #         'author': quote.css("small.author::text").extract_first(),
        #         'tags': quote.css("div.tags > a.tag::text").extract()
        #     }

        # next_page_url = response.xpath(
        #     '//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
