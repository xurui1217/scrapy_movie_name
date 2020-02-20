# -*- coding: utf-8 -*-
import scrapy
from MovieSpider.items import MoviespiderItem


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['ygdy8.net']
    # 这里写上你要爬取的页面
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    # 爬取的方法
    def parse(self, response):
        # 注意在上面导入MoviespiderItem包
        item = MoviespiderItem()
        # 匹配
        for jobs_primary in response.xpath('//table[@class="tbspan"]'):
            item['name'] = jobs_primary.xpath(
                './tr/td/b/a[2]/text()').extract()
            item['url'] = jobs_primary.xpath('./tr/td/b/a[2]/@href').extract()
            # 不能使用return
            yield item

        new_links = response.xpath('//a[text()="下一页"]/@href').extract()
        if new_links and len(new_links) > 0:
            # 获取下一页的链接
            new_link = new_links[0]
            # 再次发送请求获取下一页数据
            yield scrapy.Request("https://www.ygdy8.net/html/gndy/china/" + new_link, callback=self.parse)
