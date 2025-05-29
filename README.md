# PROJET KAYAK - DATA COLLECTION TO RECOMMEND BEST TRAVEL DESTINATIONS & HOTELS

Project completed as part of my Data Science Fullstack training at Jedha (Paris). 

## Project 🚧

<a href="https://www.kayak.com" target="_blank">Kayak</a> is a travel search engine that helps user plan their next trip at the best price.

The marketing team needs help on a new project. After doing some user research, the team discovered that **70% of their users who are planning a trip would like to have more information about the destination they are going to**. 

In addition, user research shows that **people tend to be defiant about the information they are reading if they don't know the brand** which produced the content. 

Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

* Weather 
* Hotels in the area 

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time. 

## How I carried out this project : 🎯

* I called APIs to get weather information for each destinations
* I selected top best destinations regarding current weather
* I scrapped Booking to collect information about hotels in the top destinations
* I stored all the information above in a data lake on AWS S3
* I extracted, transformed and loaded cleaned data from a datalake to a data warehouse


## Deliverable 📬

* A `.csv` file stored in an S3 bucket containing enriched information about weather and hotels for each french city

* A SQL Database where we should be able to get the same cleaned data from S3 

* Map of Top-5 destinations with best weather
![image](https://github.com/user-attachments/assets/e09be309-8b74-4435-a6f3-30f7a6b0eba9)

* Map of hotels with rating in the top-5 destinations
![image](https://github.com/user-attachments/assets/b5d299dc-e28e-488a-ba94-25e1edc2974e)



