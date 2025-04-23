import os 
import scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
import logging
import urllib.parse



best_cities_list=[
    'Gorges du Verdon',
    'Nimes',
    'Marseille',
    'Avignon',
    'Cassis'
]

class Hotel_Spider(scrapy.Spider):
    name = 'hotel_scraper'
    start_urls = [#liste des url à partir des quels on va scraper
        'https://www.booking.com/searchresults.html?ss=' + urllib.parse.quote(city) for city in best_cities_list
    ]

    def parse(self,response):
        hotel_name = response.css("div.f6431b446c.a15b38c233 ::text")
        hotel_url = response.css("a.a78ca197d0 ::attr(href)")

        for hotel_name, hotel_url in zip (hotel_name, hotel_url):
            yield {
                'city' : urllib.parse.unquote(response.url[response.url.find('ss=')+len('ss='):]),
                'hotel_name' : hotel_name.get(),
                'hotel_url': hotel_url.get(),
            }
        
# Name of the file where the results will be saved
filename = "booking_hotels.json"

#If file already exists, delete it before crawling (because Scrapy will 
#concatenate the last and new results otherwise)
if filename in os.listdir('data/'):
        os.remove('data/' + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/106.0.5249.62',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'data/' + filename : {"format": "json"},
    }
})

process.crawl(Hotel_Spider)
process.start()

