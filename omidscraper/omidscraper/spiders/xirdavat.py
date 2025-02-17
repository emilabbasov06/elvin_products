import scrapy
from ..items import XirdavatItem


class XirdavatSpider(scrapy.Spider):
    name = "xirdavat"
    allowed_domains = ["omid.az"]
    start_urls = ["https://omid.az/catalog/xirdavat%20el%20aletleri/"]

    def parse(self, response):
        items = response.css('div.catalog-section-item-content')
        
        for item in items:
            xirdavat_item = XirdavatItem()
            xirdavat_item['name'] = str(item.css('div.catalog-section-item-name').css('a.catalog-section-item-name-wrapper::text').get()).strip()
            # xirdavat_item['price'] = str(item.css('div.catalog-section-item-price-discount').css('span::text').get()).strip()
            
            price_strike = item.css('div.catalog-section-item-price-discount strike::text').get()
            price_span = item.css('div.catalog-section-item-price-discount span::text').get()

            if price_strike:
                xirdavat_item['price'] = str(price_strike).strip()
            else:
                xirdavat_item['price'] = str(price_span).strip()

            yield xirdavat_item
        
        
        for i in range(2, 59):
            yield response.follow(self.start_urls[0] + '?PAGEN_1=' + str(i), callback=self.parse)