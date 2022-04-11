d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list=[]
for i in d:
    j=0
    while j<len(d[i]):
        dict={}
        if i=="Science":
            dict[i]=d[i][j]
            list.append(dict)
        if i=="Language":
            dict[i]=d[i][j]
            list.append(dict)
        j+=1
print(list)
            
        