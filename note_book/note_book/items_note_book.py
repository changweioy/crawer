# -*- coding: utf-8 -*-
__author__ = 'changwei'

from scrapy.item import Item, Field


class NoteBookItem(Item):
    #笔记本商品信息:型号,价格,销量,商家,样品图片
    model = Field()
    price = Field()
    sales = Field()
    dealer = Field()
    pic = Field()
