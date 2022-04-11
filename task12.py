import requests
from bs4 import BeautifulSoup
import json
movieurl="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
movieName="toy_story_4"
list=[]
def scrape_movie_cast(moviceName,movieurl):
    movieurl1=requests.get(movieurl)
    data=BeautifulSoup(movieurl1.text,"html.parser") 
    mainDiv=data.find("div",class_="castSection")
    castDiv=mainDiv.find_all("div",class_="media-body")
    dic={}
    dic1={}
    l=[]
    for i in castDiv:
        M=i.span.text
        N=M.split()
        X=N[0].replace(",","").strip()
        Y=" "
        k= N[1].replace(",","").strip()
        Z=X+Y+k
        list.append(Z)
    dic["Cast_Name"]=list
    print(dic)
    with open("task12.json","w+")as f:
        json.dump(dic,f,indent=3)
    return dic

scrape_movie_cast("toy_story_4","https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")