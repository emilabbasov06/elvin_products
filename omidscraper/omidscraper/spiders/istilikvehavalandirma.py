import scrapy
from ..items import IstilikVeHavalandirmaItem


class IstilikvehavalandirmaSpider(scrapy.Spider):
    name = "istilikvehavalandirma"
    allowed_domains = ["omid.az"]
    start_urls = ["https://omid.az/catalog/istilik_ve_havalandirma/"]

    def parse(self, response):
        items = response.css('div.catalog-section-item-content')
        
        for item in items:
            istilik_ve_havalandirma_item = IstilikVeHavalandirmaItem()
            istilik_ve_havalandirma_item['name'] = str(item.css('div.catalog-section-item-name').css('a.catalog-section-item-name-wrapper::text').get()).strip()
            # istilik_ve_havalandirma_item['price'] = str(item.css('div.catalog-section-item-price-discount').css('span::text').get()).strip()
            
            price_strike = item.css('div.catalog-section-item-price-discount strike::text').get()
            price_span = item.css('div.catalog-section-item-price-discount span::text').get()

            if price_strike:
                istilik_ve_havalandirma_item['price'] = str(price_strike).strip()
            else:
                istilik_ve_havalandirma_item['price'] = str(price_span).strip()

            yield istilik_ve_havalandirma_item
        
        
        for i in range(2, 9):
            yield response.follow(self.start_urls[0] + '?PAGEN_1=' + str(i), callback=self.parse)

