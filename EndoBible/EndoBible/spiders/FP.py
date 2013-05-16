from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url

#######
#
# The spider to extract all items and raw data from
# fpnotebook endocrinology section.
#
####

from EndoBible.items import FP_Item

class FP_Spider(BaseSpider):
	name = "FP"
	allowed_domains = ["fpnotebook.com"]
	start_urls = [
		"http://www.fpnotebook.com/Endo/"
		#"http://www.fpnotebook.com/endo/Lab/index.htm"
	]

# NOW ENTERING THE CHAPTER LIST
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		chapters = hxs.select("//dt/a")
		for chapter in chapters:
			FP_Chapter_name = chapter.select("text()").extract()
			FP_SubChap_url = chapter.select("@href").extract() 
			# Need to transform the relative URLs in a_bsolutes.
			aFP_SubChap_url = [urljoin_rfc(get_base_url(response), x) for x in FP_SubChap_url]
			for url in aFP_SubChap_url:
	    			yield Request(url, callback=self.parse_chapter)

	

## NOW ENTERING THE CHAPTER DETAIL
	def parse_chapter(self, response):
		self.log("I started %s" % response.url)
		items = []
		hxs = HtmlXPathSelector(response)
		# On choppe tout ce qui traine avant la barre de separation
		Bold = hxs.select("//div[@id='toc_chap']/ul/hr/preceding-sibling::li")
		for InfoPart in Bold:
			TitreGras = InfoPart.select("text()").extract()
			# On splitte le contenu de ca
			subItems = InfoPart.select("ul/li")
			for subItem in subItems:
				item = FP_Item()
				item['FP_SubChap_url'] = response.url
				item['FP_SubChap_name'] = hxs.select('//h2/text()').extract() 
				FP_SubChap_LinkTo = subItem.select("a/@href").extract()
				# Again, let's save the full link
				aFP_SubChap_LinkTo = [urljoin_rfc(get_base_url(response), x) for x in FP_SubChap_LinkTo]
				item['FP_SubChap_LinkTo'] = aFP_SubChap_LinkTo
				item['FP_Condition_name'] = subItem.select("a/text()").extract()
				# Et on crawle les URLs avec le dernier spider.
				for url in aFP_SubChap_LinkTo:
					self.log("Lancement %s" % url)
	    				yield Request(url, meta={'item':item}, callback=self.parse_details)
				items.append(item)


## NOW ENTERING THE CHAPTER DETAIL
	def parse_details(self, response):
		hxs = HtmlXPathSelector(response)
		item = response.meta["item"]
		item['FP_Condition_name_check'] = hxs.select("//div[@class='umls']/table/tr/th/h3/text()").extract()	# pour le nom
		item['FP_Condition_ID'] = hxs.select("//div[@class='umls']/table/tr/th/h3/a/i/text()").extract()	# pour l'ID
		item['FP_Condition_aka'] = hxs.select("//div[@id='pageTitleBar']/em/text()").extract() 
		# On scrape l'arbre de details de maniere brute.
		# Ca sera processe par la suite par un spider de type FPTree.		
		item['FP_Condition_Tree'] = hxs.select("//div[@id='mainContent_text']/ol").extract()
		# On scrape les UMLS tree de maniere brute.
		# Ca sera processe par la suite par un spider de type FPUMLS.
		item['FP_UMLS_Trees'] = hxs.select("//div[@class='umls']").extract()
		# On loggue...  juste pour verifier que l'araignee ne dort pas.
		self.log("Visited detail %s" % item['FP_Condition_ID'])
		return item


