import json
import requests
from bs4 import BeautifulSoup

url=("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")

main=requests.get(url)
soup=BeautifulSoup(main.text,"html.parser")
# print(soup)

def scrape_top_list():
    list=[]
    mainbody=soup.find("div",class_="body_main container")
    table=mainbody.find("table",class_="table")
    tableall=table.find_all('tr')
    for i in tableall:
        # print(i)
        dict={}
        alltable=i.find_all("td")
        # print(alltable)
        for j in alltable: 
            rank=i.find('td',class_="bold").get_text()[:-1]
            dict["rank"]=int(rank)

            
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dict["rating"]=int(rating)
            
            review=i.find("td",class_="right hidden-xs").get_text()
            dict["review"]=int(review)
            
            movieName=i.find("a",class_="unstyled articleLink")["href"][3:]
            dict["movieName"]=movieName
            
            moviceurl=i.find("a",class_="unstyled articleLink")["href"]
            m="https://www.rottentomatoes.com"+moviceurl
            dict["moviceurl"]=m
            
            Year=i.find('a',class_="unstyled articleLink").text
            year1=Year.strip()
            
            dict["Year"]=int(Year[-5:-1])
        # print(dict)
        list.append(dict.copy())
        if {} in list:
            list.remove({})
        # print(list)
    with open("task1.json","w+") as file:
        json.dump(list,file,indent=4)
    return list
movie_data=scrape_top_list()