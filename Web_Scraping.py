# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 21:15:32 2022

@author: amrit
"""

import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="

page_num_MAX = 3

for page_num in range(1, page_num_MAX):

    req = requests.get(oyo_url, "page_num")
    content = req.content
    
    soup = BeautifulSoup(content, "html.parser")
    
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    
    scrapedinfo_list = []
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streesAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice__finalPrice"}).text
        
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
        
        amenities_list = []
        
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
                                  
        hotel_dict["amentities"] = ', '.join(amenities_list[:-1])
            
        scrapedinfo_list.append(hotel_dict)
        
        #print(hotel_name, hotel_address, hotel_price, hotel_rating, amenities_list)
        
dataFrame = pandas.DataFrame(scrapedinfo_list)
dataFrame.to_csv("OYO.csv")