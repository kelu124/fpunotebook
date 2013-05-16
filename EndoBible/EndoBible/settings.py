# Scrapy settings for EndoBible project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'EndoBible'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['EndoBible.spiders']
NEWSPIDER_MODULE = 'EndoBible.spiders'
DEFAULT_ITEM_CLASS = 'EndoBible.items.EndobibleItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


# Store
FEED_URI='mycrawler-results.xml'
FEED_FORMAT='xml'

