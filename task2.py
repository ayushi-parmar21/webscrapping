import json
from task1 import scrape_top_list
movies=scrape_top_list()
def group_by_year(movies):
    dict1={}
    for i in movies:
        movie_year=[]
        year=i["Year"]
        if year not in dict1:
            for j in movies:
                # print(j)
                if j["Year"]==year:
                    movie_year.append(j)
                dict1[year]=movie_year
        with open("task2.json","w+") as movie_data:
            json.dump(dict1,movie_data,indent=4)
    
    return dict1

group_by_year(movies)