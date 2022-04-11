import json
import requests
from bs4 import BeautifulSoup

url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def movie_details(movies_url):
    rest=requests.get(movies_url)
    soup= BeautifulSoup(rest.text,"html.parser")
    h1=soup.find("h1",class_="scoreboard__title").get_text()
    li=soup.find_all("li",class_="meta-row clearfix")
    dict={}
    dict["Name"]=h1
    for i in li:
        file=i.text
        b=file.split()
        if "Rating:" in b:
            dict["Rating"]=b[1]
        elif "Genre:" in b:
            # dict["Genre"]=b[1:]
            w=b[1:]
            h=" "
            i=0
            while i<len(w):
                h=h+w[i]
                i+=1
            l=h.split(",")
            k=" "
            r={}
            l1=[]
            for i in l:
                str1=" "
                for j in i:
                    if j!=k:
                        str1+=j
                l1.append(str1)
            dict["Genre"]=l1
        elif "Language:" in b:
            dict["Language"]=b[2]
        elif "Director:" in b:
            w=b[1:]
            h=" "
            i=0
            while i<len(w):
                h=h+w[i]
                i+=1
            l=h.split(",")
            k=" "
            r={}
            l1=[]
            for i in l:
                str1=" "
                for j in i:
                    if j!=k:
                        str1+=j
                l1.append(str1)
            dict["Director"]=l1
        elif "Producer:" in b:
            dict["Producer"]=b[1:]
        elif "Runtime:" in b:
            s=b[1:]
            for i in s:
                if "h" in i:
                    first=int(i[0:-1])*60
                elif "m" in i:
                    sec=int(i[:-1])
            dict["Runtime"]=first+sec
    with open("task4.json","w+") as file:
        json.dump(dict,file,indent=4)
    # print(dict)
    return dict
movie_details(url)