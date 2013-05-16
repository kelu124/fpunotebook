from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from EndoBible.items import EndobibleCondItem

#######
#
# The spider to extract all items and raw data from
# endobible, dans la partie Conditions.
#
####

class EndoCSpider(BaseSpider):
	name = "endoc"
	allowed_domains = ["endobible.com"]
	start_urls = [
		"http://www.endobible.com/conditions/"
	]


	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		Glandes = hxs.select('//h2') 
		for glande in Glandes:
			item = EndobibleCondItem()
			item['CURL'] = response.url
			item['CGlande'] = glande.select('text()').extract()
			GListe = glande.select('following-sibling::ul')
 			for condition in GListe.select('li'):	
				item['CCondName'] = condition.select('a/text()').extract()
				url = condition.select('a/@href').extract()
				#self.log("Condition: %s" % item['CCond'])
				#self.log("URL() : %s" % url)
	    			yield Request(url[0], meta={'item':item}, callback=self.parse_Top)
				
			items.append(item)
			
			
	def parse_Top(self, response):
		item = response.meta["item"]
		item['CURLTop'] = response.url
		hxs = HtmlXPathSelector(response)
		top = hxs.select('//ul[@class="pathway"]/li/a/@href').extract()
		item['CLiens'] = top
		yield Request(top[0], meta={'item':item}, callback=self.parse_His)
		yield Request(top[1], meta={'item':item}, callback=self.parse_Exa)
		yield Request(top[2], meta={'item':item}, callback=self.parse_Inv)
		yield Request(top[3], meta={'item':item}, callback=self.parse_Mgt)

	def parse_His(self, response):
		item = response.meta["item"]
		item['CURLHis'] = response.url
		hxs = HtmlXPathSelector(response)
		item['CQueHis'] = hxs.select('//div[@class="contentBox"]/h2[@class="question"]/text()').extract() 
		item['CAnsHis'] = hxs.select('//div[@class="contentBox"]/div[@class="answer"]//text()').extract()

	def parse_Exa(self, response):
		item = response.meta["item"]
		item['CURLExa'] = response.url
		hxs = HtmlXPathSelector(response)
		item['CQueExa'] = hxs.select('//div[@class="contentBox"]/h2[@class="question"]/text()').extract() 
		item['CAnsExa'] = hxs.select('//div[@class="contentBox"]/div[@class="answer"]//text()').extract()
		
	def parse_Inv(self, response):
		item = response.meta["item"]
		item['CURLInv'] = response.url
		hxs = HtmlXPathSelector(response)
		item['CQueInv'] = hxs.select('//div[@class="contentBox"]/h2[@class="question"]/text()').extract() 
		item['CAnsInv'] = hxs.select('//div[@class="contentBox"]/div[@class="answer"]//text()').extract()


	def parse_Mgt(self, response):
		item = response.meta["item"]
		item['CURLMgt'] = response.url
		hxs = HtmlXPathSelector(response)
		item['CQueMgt'] = hxs.select('//div[@class="contentBox"]/h2[@class="question"]/text()').extract() 
		item['CAnsMgt'] = hxs.select('//div[@class="contentBox"]/div[@class="answer"]//text()').extract()

		return item



