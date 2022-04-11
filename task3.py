import json
with open("task2.json","r+") as file:
    data=json.load(file)

# movies=moviedata()
def group_by_year(movies):
    list1=[]
    dic={}
    for i in movies:
        mod=int(i)%10
        decade=int(i)-mod
        if decade not in list1:
            list1.append(decade)


    list1.sort()   
    for i in list1:  
        dic[i]=[]
        k=0
    for i in dic:
        dic10=i+9
        for x in movies:
            if int(x)<=dic10 and int(x)>=i:
                for v in movies[x]:
                    dic[i].append(v)
    with open("task3.json","w+") as year_info:
        json.dump(dic,year_info,indent=4)
    return dic
group_by_year(data)
