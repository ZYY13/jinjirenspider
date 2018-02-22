# -*- coding:utf-8 -*-

import time
import re
import requests
import urllib
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from weibo.items import JingjirenItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule


class Spider(CrawlSpider):

     name = "WeiboSpider"
     start_urls=["http://www.todgo.com/shjjr/gr-P2474.html"]



     def parse(self, response):

        item = JingjirenItem()
        modules = response.xpath('//*[@class="jjrbox left"] | //*[@class="jjrbox right"]')

        for module in modules:
            item["name"] = module.xpath('string(dd[1]/strong/a)')
            item["company"] = module.xpath('string(dd[2]/a)')
            if (module.xpath('string(dd[5]/text())').extract()[0]):
                item["phonenum"] = module.xpath('string(dd[5]/text())')
            else:
                item["phonenum"] = module.xpath('string(dd[4]/text())')


            if (item["name"].extract()[0]  or item["company"].extract()[0]  or item["phonenum"].extract()[0]):
                item["name"] = item["name"].extract()[0]
                item["company"] = item["company"].extract()[0]
                item["phonenum"] = item["phonenum"].extract()[0]
                yield item
                time.sleep(0.1)
            else:
                print("此条记录为空")



        nextpages = response.xpath(u"/html/body/div[6]/a[text()='下一页']")
        if (nextpages):
            result = nextpages.extract()[0]
            pattern = re.compile("\d+")
            num = re.search(pattern, result).group(0)
            print num
            url = "http://www.todgo.com/shjjr/gr-P" + num + ".html"
        else:
            print("已到最后一页")
        yield Request(url, callback=self.parse)































