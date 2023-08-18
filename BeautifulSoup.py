'''
import requests
from bs4 import BeautifulSoup
url="https://www.flipkart.com/search?q=nintendo+switch&sid=4rr%2Cx1m&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=nintendo+switch%7CGaming+Consoles&requestId=36da7d0b-9353-4f65-a38c-0480b2122d9c&as-searchtext=ninte"

data=requests.get(url)
#print(data)


plain_text=data.text
#print(plain_text)
res=BeautifulSoup(plain_text,"html.parser")
#print(type(res))



a=res.findAll("div",{"class":"_30jeq3"})
print(a)
'''

'''
for i in a:
    print(i.text)
    print("*"*50)
'''



  


#1000 to 20000 thousand middle price    nintendo price
'''
for i in range(5001,20000):
    print(i)
    
numbers=[ i for a  in 
         range(5001,10000)]
print(i)
'''



import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=nintendo+switch&sid=4rr%2Cx1m&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=nintendo+switch%7CGaming+Consoles&requestId=36da7d0b-9353-4f65-a38c-0480b2122d9c&as-searchtext=ninte"
data=requests.get(url)
#print(data)


plain_text=data.text
#print(plain_text)

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")


a=soup.findAll("div",{"class":"_30jeq3"})






for i in a:
     k=i.text.replace("₹","")
     m=k.replace(",","")
     if int(m)>10000:
         print(m)
     
         print("*"*50)





'''
prices = []

for i in soup.find_all("div", class_="_30jeq3"):
    prices.append(i.text)
print(i)
'''
      

    
    
        
       
           
         

