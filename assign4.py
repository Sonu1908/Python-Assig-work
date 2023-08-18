#Q1
people ={1: {'name': 'John', 'age': '27', 'gender': 'Male'},
2: {'name': 'Marie', 'age': '22', 'gender': 'Female'},
3: {'name': 'Luna', 'age': '24', 'gender': 'Female'},
4: {'name': 'Peter', 'age': '29', 'gender':'Male'}}

a=people.pop(3)
print(people)







#Q2

data={'a':1,'c': {'m':2,'n':{'x':5,'y':[7,8,9]}},'d':[1,2,3]}
#b=data.values()
#print(data.values())

value1=(data['c']['n']['x'])
value2=(data['c']['m'])
value3=(data['c']['n']['y'][1])
print(value1,value2,value3)

'''
print(data['c']['n']['x'])
print(data['c']['m'])
print(data['c']['n']['y'][1])
'''
