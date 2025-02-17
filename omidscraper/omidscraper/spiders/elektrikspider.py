import scrapy
from ..items import ElektrikItem

class ElektrikspiderSpider(scrapy.Spider):
    name = "elektrikspider"
    allowed_domains = ["omid.az"]
    start_urls = ["https://omid.az/catalog/elektrik/"]

    def parse(self, response):
        items = response.css('div.catalog-section-item-content')
        
        for item in items:
            elektrik_item = ElektrikItem()
            elektrik_item['name'] = str(item.css('div.catalog-section-item-name').css('a.catalog-section-item-name-wrapper::text').get()).strip()
            # elektrik_item['price'] = str(item.css('div.catalog-section-item-price-discount').css('span::text').get()).strip()
            
            price_strike = item.css('div.catalog-section-item-price-discount strike::text').get()
            price_span = item.css('div.catalog-section-item-price-discount span::text').get()

            if price_strike:
                elektrik_item['price'] = str(price_strike).strip()
            else:
                elektrik_item['price'] = str(price_span).strip()

            yield elektrik_item
        
        
        for i in range(2, 48):
            yield response.follow(self.start_urls[0] + '?PAGEN_1=' + str(i), callback=self.parse)