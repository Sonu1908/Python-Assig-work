import pandas as pd


data=pd.read_csv("movie.csv")
#print(data)

#Q1..
#print(data[data["Director"]=="Ridley Scott"])


#Q2..
#print(data["Director"]=="Ridley Scott")

#print(data[(data["Director"]=="Ridley Scott") &(data["Rating"]>7)])

#print(data)





#Q3...

print(data[(data["Year"]>=2005) &(data["Year"]<=2010)&(data["Rating"]>8)])
#data=data[data["Rating"]>8]







#Q4...
#print(data.columns.values)   


data["rating_category"]=data["Rating"].apply(lambda x: "good" if x>8 else "bad")
print(data)

