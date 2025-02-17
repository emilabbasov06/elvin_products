# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class OmidscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        price_string = adapter.get('price')
        if price_string == '':
            adapter['price'] = 0
        else:
            price_string = str(price_string).replace(' ₼', '')
            price_string = price_string.strip()
            adapter['price'] = float(price_string)

        return item
    
    
    
    
    
import mysql.connector

class SaveToMySQLPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin_001",
            database="elvin_products",
            charset="utf8mb4",
            collation="utf8mb4_general_ci"
        )

        
        self.cur = self.conn.cursor()
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS elektrik (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2)
        )
        """)
    
    def process_item(self, item, spider):

        self.cur.execute(""" insert into elektrik (
            name, 
            price
            ) values (
                %s,
                %s
                )""", (
            item["name"],
            item["price"]
        ))
        
        self.conn.commit()
        return item

    
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()