from random import randrange
name=["Product1","Product2","Product3","Product4","Product5"]
type=["Food", "Electronic", "Drink", "Outdoors","Toys"]
location=[1,2,3,4,5,6,7,8,9]

count = 0
while count < 20:
    print("{",name[randrange(0,len(name))],",",type[randrange(0,len(type))],",",location[randrange(0,len(location))],"}")
    count+=1
