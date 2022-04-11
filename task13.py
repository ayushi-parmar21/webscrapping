import json
from shutil import move
import requests
from bs4 import BeautifulSoup
from task4 import movie_details
from task12 import scrape_movie_cast

movie_cast=scrape_movie_cast("toy_story_4","https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")
movie_detail=movie_details("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")
list=[]

def movies_details_cast():
    list.append(movie_detail)
    list.append(movie_cast)
    with open("task13.json","w+")as f:
        json.dump(list,f,indent=3)
    return list
movies_details_cast()
    
    
