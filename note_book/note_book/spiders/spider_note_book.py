#-*- coding: utf-8 -*-
__author__ = 'changwei'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ..items_note_book import NoteBookItem
import sys


class NoteBookTaoBaoSpider(BaseSpider):
    name = "notebook"
    allowed_domains = ["taobao.com"]
    start_urls = ['http://spu.taobao.com/spu/3c/spulist.htm?spm=a310c.2169925.5642977.%d.X7uVGp&cat=1101&page=%d' % (x+1, x+1) for x in xrange(50)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="choices-item"]/ul/li')
        #sites = hxs.select('//div')
        print "sites length: %s" % len(sites)
        items = []

        for site in sites:
            item = NoteBookItem()
            item['pic'] = 'none'
            #item['pic'] = site.select('div[@class="pic"]/a/@href').extract()
            item['model'] = site.select('div[@class="title"]/p[1]/a/strong/b/text()').extract()
            item['price'] = site.select('div[@class="title"]/p[2]/span/em/text()').extract()
            item['sales'] = site.select('div[@class="title"]/p[2]/text()').extract()
            item['dealer'] = 'www.taobao.com'
            '''
            print '################start######################'
            print 'model = ', item['model']
            print 'price = ', item['price']
            print 'sales = ', item['sales']
            print 'dealer = ', item['dealer']
            print 'pic = ', item['pic']
            print '################end########################'
           '''
            items.append(item)
        return items


class NoteBookSpider(BaseSpider):
    name = "notebook"
    allowed_domains = ["jd.com"]
    start_urls = ['http://list.jd.com/list.html?cat=670,671,672']

    def parse(self, response):
        print '###########response#####################'
        print response
        print '########################################'
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        print 'here'
        for site in sites:
            item = NoteBookItem()
            item['model'] = site.select('.//div[@class=''p-name'']/a/@title').extract()
            item['price'] = site.select('.//div[@class=''p-price'']/strong/text()').extract()
            item['sales'] = 'none'  # js描述的,暂时获取不到
            item['dealer'] = 'jd.com'
            item['pic'] = site.select('.//div[@class=''p-img'']/a/img/@src').extract()
            print 'model = ', item['model']
            print 'price = ', item['price']
            print 'sales = ', item['sales']
            print 'dealer = ', item['dealer']
            print 'pic = ', item['pic']
            items.append(item)
        return items