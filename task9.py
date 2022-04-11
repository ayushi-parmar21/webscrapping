import json
import time
import requests 
import os 
import random
from task1 import scrape_top_list

T1=scrape_top_list()
with open("task1.json","r+") as file9:
    a=json.load(file9)
def txt(a):
    random_s=random.randint(1,3)
    for i in a:
        # print(i)
        path=("/home/dell39/python/web scraping/wabscrapping"+i["movieName"]+".json")
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell39/python/web scraping/wabscrapping"+i["movieName"]+".json","w")
            url=requests.get(i["moviceurl"])
            create1=create.write(url.text)
            create.close()
        time.sleep(random_s)
txt(a)
