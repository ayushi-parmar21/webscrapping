from itertools import count
import json
with open("task5.json","r")as file:
    data=json.load(file)
def anlyse_movie_genre(data):
    dict={}
    list=[]
    for i in data:
        count=0
        for j in i:
            if "Genre" in i:
                gen=i["Genre"]
                for k in range(len(gen)):
                    list.append(gen[k])
                    for l in range(len(gen)):
                        if gen[k]==gen[l]:
                            count+=1
                    dict[gen[k]]=count      
            else:
                continue
    # print(dict)
    with open("task11.json","w+")as f:
        json.dump(dict,f,indent=3)
        return dict
anlyse_movie_genre(data)