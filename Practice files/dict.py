thisdict={
    "name":"Umang",
    "age":19,
    "course":"BCA"
    }
lst=[]
print(thisdict)
for x in thisdict:
    lst.append(x)
    print(thisdict[x])
thisdict["course"]="BBA"
print(len(thisdict))
