import json
import requests 
import os 
with open("task1.json","r+") as file8:
    a=json.load(file8)
    # print(a)
def txt(a):
    for i in a:
        # print(i)
        path=("/home/dell39/python/web scraping/wabscrapping"+i["movieName"]+".text")
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell39/python/web scraping/wabscrapping"+i["movieName"]+".text","w")
            url=requests.get(i["moviceurl"])
            create1=create.write(url.text)
            create.close()
txt(a)