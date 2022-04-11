import json
from task1 import scrape_top_list
from task4 import movie_details
 
all_movies=scrape_top_list()
top_movies=all_movies[:100]
def get_movies_details_list():
    list1=[]
    for i in top_movies:
        for j in i:
            # print(j)
            if j=="moviceurl":
                list1.append(movie_details(i[j])) 
    # print(list1)
    with open("task5.json","w+") as files:
        json.dump(list1,files,indent=4)
    return list1
get_movies_details_list()