import json
data=open("task5.json","r+")
a=json.load(data)
list=[]
d=a[:51]
def analyse_language_and_directors(movie_list):
    director_dic={}
    for movie in movie_list:
        for director in movie["Director"]:
            director_dic[director]={}
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]=0
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]+=1
    # with open("task10.json","a") as file:
    #     list.append(director_dic)
    #     json.dump(list,file,indent=4)
    #     return list
    list.append(director_dic)
analyse_language_and_directors(d)
d=a[53:55]
def analyse_language_and_directors(movie_list):
    director_dic={}
    for movie in movie_list:
        for director in movie["Director"]:
            director_dic[director]={}
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]=0
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]+=1
    # with open("task10.json","a") as file:
    #     list.append(director_dic)
    #     json.dump(list,file,indent=4)
    #     return list
    list.append(director_dic)
analyse_language_and_directors(d)
d=a[57:]
def analyse_language_and_directors(movie_list):
    director_dic={}
    for movie in movie_list:
        for director in movie["Director"]:
            director_dic[director]={}
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]=0
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["Director"]:
                language=movie_list[i]["Language"]
                director_dic[director][language]+=1
    with open("task10.json","a") as file:
        list.append(director_dic)
        json.dump(list,file,indent=4)
        return list
analyse_language_and_directors(d)

