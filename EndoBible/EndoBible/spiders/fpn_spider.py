from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url

#all_links = hxs.select('//a/@href').extract()
#abs_links = [urljoin_rfc(get_base_url(response), x) for x in all_links]

from EndoBible.items import FPN_Item

class FPN_Spider(BaseSpider):
	name = "fpn"
	allowed_domains = ["fpnotebook.com"]
	start_urls = [
		"http://www.fpnotebook.com/Endo/Thyroid/index.htm"
		#"http://www.fpnotebook.com/endo/Lab/index.htm"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		Bold = hxs.select("//div[@id='toc_chap']/ul/li") # on recupere les titres
		self.log("Parsed %s" % Bold)
		for InfoPart in Bold:
			subList = Bold.select("ul/li")
			self.log("Parsed %s" % subList)
			for subItem in subList:
				item = FPN_Item()	
				item['FPN_source_url'] = response.url
				item['FPN_source_title'] = hxs.select('//h2/text()').extract() 
				item['FPN_link'] = subItem.select("a/@href").extract()
				item['FPN_name'] = subItem.select("a/text()").extract()
				self.log("Parsed %s" % item['FPN_name'])
				items.append(item)
		return items

		




