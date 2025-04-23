import os 
import scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
import logging
import urllib.parse
import pandas as pd

data=pd.read_csv('data/top_best_weather.csv')
best_cities_list=data["cities"].to_list()

class HotelSpider(scrapy.Spider):
    name = 'hotel_scraper'
    start_urls = [#liste des url à partir des quels on va scraper
        'https://www.booking.com/searchresults.html?ss=' + urllib.parse.quote(city) for city in best_cities_list
    ]

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3; fr-FR'
        }
    }

    def parse(self,response):
        hotel_names = response.css("div.f6431b446c.a15b38c233 ::text").getall()
        hotel_urls = response.css("a.a78ca197d0 ::attr(href)").getall()
        city = urllib.parse.unquote(response.url[response.url.find('ss=') + len('ss='):])

        for hotel_name, hotel_url in zip(hotel_names, hotel_urls):
            full_url = response.urljoin(hotel_url)
            # Envoyer une nouvelle requête pour chaque URL d'hôtel avec les informations de base
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_hotel,
                meta={'city': city, 'hotel_name': hotel_name}
            )
    
    def parse_hotel(self, response):
            # Récupérer les informations de base passées via meta
            city = response.meta['city']
            hotel_name = response.meta['hotel_name']

            # Extraire les informations détaillées de l'hôtel
            hotel_rating = response.css("div.ac4a7896c7::text").get()
            hotel_address = response.css("div.a53cbfa6de.f17adf7576::text").get()
            hotel_description = response.css("p.a53cbfa6de.b3efd73f69::text").get()
            latlng = response.css('a#map_trigger_header_pin::attr(data-atlas-latlng)').get()

            latlng_cleaned = latlng.replace('\u200b', '').replace(' ', '').strip()
            lat, lon = latlng_cleaned.split(',')


            if hotel_rating and hotel_address and hotel_description and latlng:
                yield {
                    "city": city,
                    "hotel_name": hotel_name,
                    "hotel_address": hotel_address,
                    'latitude' : lat,
                    'longitude' : lon,
                    "hotel_rating": hotel_rating.split()[-1],
                    "hotel_description": hotel_description,
                    "hotel_url": response.url
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

process.crawl(HotelSpider)
process.start()

