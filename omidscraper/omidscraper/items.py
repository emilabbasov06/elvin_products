# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OmidscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ElektrikItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()


class SantexnikaItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    

class IstilikVeHavalandirmaItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()


class XirdavatItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()