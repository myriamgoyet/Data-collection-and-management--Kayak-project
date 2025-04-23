import os 
import scrapy
from scrapy import Selector
from scrapy.crawler import CrawlerProcess
import logging

class Hotel_Spider(scrapy.Spider):
    name = 'hotel_scraper'
    start_urls = [#liste des url à partir des quels on va scraper
        "https://www.booking.com/searchresults.fr.html?ss=aigues&efdco=1&label=qwa121jc-1DCAEoggI46AdIM1gDaE2IAQGYAQ24ARfIAQ_YAQPoAQGIAgGoAgO4AoX3mr8GwAIB0gIkMDk1NzlmY2YtNjcwMy00MzdkLWFmNGItMzE3ODQzYzYxNWI32AIE4AIB&sid=f8c0b82bd17e0df0aab4997651af0857&aid=1588662&lang=fr&sb=1&src_elem=sb&src=index&dest_id=-1406800&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=fr&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=9fc26a828ac01775&ac_meta=GhA5ZmMyNmE4MjhhYzAxNzc1IAAoATICZnI6BmFpZ3Vlc0AASgBQAA%3D%3D&checkin=2025-03-28&checkout=2025-03-29&group_adults=2&no_rooms=1&group_children=0",
    ]

    def parse(self,response):
        #toutes les div dont la classe est c824.....(=l'encadré de l'autel)
        hotel = response.css('div.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4')
        return {
            'hotel_name' : hotel.css('div.f6431b446c a15b38c233')
        }

        <div data-testid="title" class="f6431b446c a15b38c233">Hôtel Le Médiéval</div>