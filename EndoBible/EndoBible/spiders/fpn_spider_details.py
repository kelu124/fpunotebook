from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from EndoBible.items import sFPN_Item

class small_FPN_Spider(BaseSpider):
	name = "sfpn" #small fpn
	allowed_domains = ["fpnotebook.com"]
	start_urls = [
		"http://www.fpnotebook.com/endo/Lab/index.htm"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		Bold = hxs.select("//div[@id='toc_chap']/ul/li") # on recupere les titres

		for InfoPart in Bold:
			subList = Bold.select("ul/li")

			for subItem in subList:
				item = FPN_Item()	
				item['FPN_source_url'] = response.url
				item['FPN_source_title'] = hxs.select('//h2/text()').extract() 
				item['FPN_link'] = subItem.select("a/@href").extract()
				item['FPN_name'] = subItem.select("a/text()").extract()

				items.append(item)
		return items

		




