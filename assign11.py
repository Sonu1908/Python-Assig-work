data=[
  {
       "id":'A1',
    "author": "Chinua Achebe",
    "country": "Nigeria",
    "imageLink": "images/things-fall-apart.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
    "pages": 209,
    "title": "Things Fall Apart",
    "year": 1958,
    "price":125
  },
  {
   "id":'A2',
    "author": "Hans Christian Andersen",
    "country": "Denmark",
    "imageLink": "images/fairy-tales.jpg",
    "language": "Danish",
    "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
    "pages": 784,
    "title": "Fairy tales",
    "year": 1836,
    "price":225
  },
  {
   "id":'A3',
    "author": "Dante Alighieri",
    "country": "Italy",
    "imageLink": "images/the-divine-comedy.jpg",
    "language": "Italian",
    "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
    "pages": 928,
    "title": "The Divine Comedy",
    "year": 1315,
    "price":345
  },
  {
   "id":'A4',
    "author": "Unknown",
    "country": "Sumer and Akkadian Empire",
    "imageLink": "images/the-epic-of-gilgamesh.jpg",
    "language": "Akkadian",
    "link": "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh\n",
    "pages": 160,
    "title": "The Epic Of Gilgamesh",
    "year": -1700,
    "price":600
  },
  {
   "id":'A5',
    "author": "Unknown",
    "country": "Achaemenid1 Empire",
    "imageLink": "images/the-book-of-job.jpg",
    "language": "Hebrew",
    "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
    "pages": 176,
    "title": "The Book Of Job",
    "year": -600,
    "price":520
  },
  {
   "id":'A6',
    "author": "Unknown",
    "country": "India/Iran/Iraq/Egypt/Tajikistan",
    "imageLink": "images/one-thousand-and-one-nights.jpg",
    "language": "Arabic",
    "link": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights\n",
    "pages": 288,
    "title": "One Thousand and One Nights",
    "year": 1200,
    "price":255
  },
  {
   "id":'A7',
    "author": "Unknown",
    "country": "Iceland",
    "imageLink": "images/njals-saga.jpg",
    "language": "Old Norse",
    "link": "https://en.wikipedia.org/wiki/Nj%C3%A1ls_saga\n",
    "pages": 384,
    "title": "Nj\u00e1l's Saga",
    "year": 1350,
    "price":115
  },
  {
   "id":'A8',
    "author": "Jane Austen",
    "country": "United Kingdom",
    "imageLink": "images/prid1e-and-prejudice.jpg",
    "language": "English",
    "link": "https://en.wikipedia.org/wiki/Prid1e_and_Prejudice\n",
    "pages": 226,
    "title": "Prid1e and Prejudice",
    "year": 1813,
    "price":295
  },
  {
   "id":'A9',
    "author": "Honor\u00e9 de Balzac",
    "country": "France",
    "imageLink": "images/le-pere-goriot.jpg",
    "language": "French",
    "link": "https://en.wikipedia.org/wiki/Le_P%C3%A8re_Goriot\n",
    "pages": 443,
    "title": "Le P\u00e8re Goriot",
    "year": 1835,
    "price":200
  },
  {
   "id":'10',
    "author": "Samuel Beckett",
    "country": "Republic of Ireland",
    "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
    "language": "French, English",
    "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
    "pages": 256,
    "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
    "year": 1952,
    "price":150
  },
 
]


class ej:
    def __init__(self,ej):
        self.a=ej
    def get_books(self):
        a=list(map(lambda x:x["title"],self.a))
        print(a)
        
        
    def sample(self,author):
        def title(demo_title):
            if(demo_title["author"]==author):              #Q..2
                print(demo_title["title"])
        list(filter(title,self.a))
        
        
    def get_price(self):
        x=list(filter(lambda x:x["price"]<300,self.a))      #Q..4
        print(x)
        
        
    def sample1(self,data1):
        def title(demo_title):
            if(demo_title["author"]==data1 or demo_title["id"]==data1):    #Q3
                print(demo_title)
        list(filter(title,self.a))
        
        
        
    def sum_books(self):
        a=list(map(lambda x:x["price"],self.a))                    #Q..5
        #print(a)
        sum=0
        for i in a:
            sum+=i   
        print(sum)
        
        
    def get_greater(self):
          x=list(filter(lambda x:x["price"]>500,self.a))              #Q..6
         # print(x)
          total= 0
          for i in x:
               if i["price"] > 500:
                   total=total+i["price"]
          print(total)

  

    
    
ob1=ej(data)
#ob1.get_books()                                 #Q1


#x=input("Enter author name: ")
#ob1.sample(x)                                    #Q2


#ob1.get_price()                                   #Q4






#x=input("Enter author name: ")
#ob1.sample1(x)                                    #Q3








#ob1.sum_books()                 #Q5
ob1.get_greater()                #Q6























