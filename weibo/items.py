# encoding=utf-8

from scrapy import Item,Field

class JingjirenItem(Item):
    id = Field()
    name = Field()
    company = Field()
    phonenum = Field()