ayu=["puja","rani"]
i=0
dict={}
while i<len(ayu):
    j=0
    key=""
    value=""
    count=0
    while j<len(ayu[i]):
        if count<=1:
            key+=ayu[i][j]
            count+=1
        else:
            value+=ayu[i][j]
        j+=1
    dict[key]=value
    i+=1
print(dict)