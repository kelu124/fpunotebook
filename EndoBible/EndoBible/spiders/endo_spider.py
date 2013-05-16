from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from EndoBible.items import EndobibleSymptomItem

#######
#
# The spider to extract all items and raw data from
# endobible, dans la partie Symptoms.
#
####

class EndoSpider(BaseSpider):
	name = "endo"
	allowed_domains = ["endobible.com"]
	start_urls = [
		"http://www.endobible.com/symptoms/"
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		items = []

		symptoms = hxs.select('//div[@class="halfRight"]/ul/li')
		for symptom in symptoms:
			item = EndobibleSymptomItem()		    
			item['Sname'] = symptom.select('a/text()').extract()
			item['Slink'] = symptom.select('a/@href').extract()
			item['Ssite'] = response.url
			self.log("Visited %s" % response.url)
 			for url in symptom.select('a/@href').extract():
            			yield Request(url, meta={'item':item}, callback=self.parse_details)
			items.append(item)

		symptoms = hxs.select('//div[@class="halfLeft"]/ul/li')
		for symptom in symptoms:
			item = EndobibleSymptomItem()		    
			item['Sname'] = symptom.select('a/text()').extract()
		#	self.log("Nom %s" % item['Sname'])
			item['Slink'] = symptom.select('a/@href').extract()
			item['Ssite'] = response.url
		#	self.log("Visited %s" % response.url)
 			for url in symptom.select('a/@href').extract():
            			yield Request(url, meta={'item':item}, callback=self.parse_details)
			items.append(item)


       	#	return items

	def parse_details(self, response):
		item = response.meta["item"]
		item['SDurl'] = response.url
#		self.log("Visited Parse2 %s" % response.url)
		hxs = HtmlXPathSelector(response)
		item['SDname'] = hxs.select("//h1/text()").extract()
		item['SDcond'] = hxs.select('//div[@class="mainContent"]/ul/li').extract()
		item['SDother'] = hxs.select("//div[@class='mainContent']/p/text()").extract()
		return item



		

