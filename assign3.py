#Q1

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#list1[2][2].insert(2,700) #2 parameter pass
list1[2][2].append(7000)
print(list1)





#Q2


tuple1 =(11, [22, 33], 44, 55)
y=list[tuple1] #list from the tuple
tuple1[1][0]=222
print(tuple1)






#append me pura list
#extend me only value
#Q3---

list2=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
#list2[2][1].insert(3,["h","i","j"])
list2[2][1][2].extend(["h","i","j"])
print(list2)



