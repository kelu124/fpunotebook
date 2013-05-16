# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class EndobibleItem(Item): # for the EndoBible project...
	EItest = Field()

class EndobibleSymptomItem(Item):
	Ssite = Field() #ok
	Sname = Field() #ok
	Slink = Field() #ok
	SDname = Field() ##ok
	SDurl = Field() ##ok
	SDcond = Field() #ok
	SDother = Field() #ok

class EndobibleCondItem(Item):
	CURL = Field() #
	CGlande = Field() # 
	CCondName = Field()  #
	CURLTop = Field()  #
	CURLHis = Field()  #
	CLiens = Field() #
	CQueHis = Field() 
	CAnsHis = Field() 
	CURLExa = Field() 
	CQueExa = Field() 
	CAnsExa = Field() 	
	CURLInv = Field() 
	CQueInv = Field() 
	CAnsInv = Field() 
	CURLMgt = Field() 
	CQueMgt = Field() 
	CAnsMgt = Field() 

class FPN_Item(Item):
	FPN_source_url = Field()  #
	FPN_source_title = Field() #
	FPN_category = Field() 
	FPN_name = Field() 
	FPN_link = Field() 

class sFPN_Item(Item):
	FPN_source_url = Field()  #
	FPN_source_title = Field() #
	FPN_category = Field() 
	FPN_name = Field() 
	FPN_link = Field() 

class FP_Item(Item):
	FP_Chapter_url = Field()  
	FP_Chapter_name = Field()
	FP_SubChap_url = Field() #
	FP_SubChap_name = Field() #
	FP_SubChap_LinkTo = Field()#
	FP_Condition_name = Field() #
	FP_Condition_name_check = Field() #
	FP_Condition_ID = Field() #
	FP_Condition_aka = Field() #
	FP_Condition_Tree = Field() #
	FP_UMLS_Trees = Field()

class FPTree_Item(Item):
	FPT_URL = Field()  #
	FPT_Name = Field() #
	FPT_Parent_name = Field() #
	FPT_Page = Field() #

class FP_ULMS_Item(Item):
	FPU_URL = Field()  #
	FPU_Page = Field()  #
	FPU_Name = Field() #
	FPU_Code = Field() #
	FPU_DefML = Field() 
	FPU_DefNCI = Field() #
	FPU_DefMSH = Field() #
	FPU_MSH = Field() #
	FPU_SnomedCT = Field() #
	FPU_DefCSP = Field() #
	FPU_Concepts = Field() #  
	FPU_Concepts_Codes = Field() # 
	FPU_LG_English = Field()  #
	FPU_LG_French = Field()  #

