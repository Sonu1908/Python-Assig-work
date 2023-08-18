#Q1
'''
per=int(input("Enter the value:="))
if(per>=80):
    print("Grade A+")

elif(per>=60 and per <80):
    print("Grade A")

elif(per>=50 and per <60):
    print("Grade B+")

elif(per>=45 and per <50):
    print("Grade B")

elif(per>=25 and per <45):
    print("Grade C")    
elif per<25:
    print("D")   
else:
    print("the valid number")

'''




#Q2three sides of a triangle and check
'''
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if(x==y and y==z):
    print("Equilateral triangle")       #x=y=z all three sides are equal.
elif(x==y or y==z or z==x):
      print("isosceles triangle")       #x=z   at least) two equal sides.
else:
	print("Scalene triangle")       #x<>y<>z    three unequal sides.
'''






#Q3
	
'''
a=int(input("enter your first:"))
if(a%3==0):

     print("num is even")
else:

     print("num is odd")	
'''	
	







#Q4
'''
month = "February"

if( month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December"):
    days = 31
elif( month == "February"):
    days = 28
elif( month == "April" or month == "June" or month == "September" or month == "November"):
    days = 30
else:
    print("Invalid month name")
    days = 0

print(f"Number of days in {month}: {days}")
 '''



#Q5
'''
a=int(input("enter your first:"))
b=int(input("enter your second:"))
c=int(input("enter your third:"))
 
if(a<b or b>a):
     print("a is number") 
elif(b>a or b>c):

    print("b is median")
else:
    print("c is number")

'''




     
#Q6 week number and print day of week
''' 
weekday =int(input("Enter weekday day number: "))

if(weekday==1):
     print("Monday")
elif(weekday==2):
     print("Tuesday")
elif(weekday==3):
     print("Wednesday")
elif(weekday==4):
     print("Thursday")
elif(weekday==5):
     print("Friday")
elif(weekday==6):
     print("Saturday")
elif(weekday==7):
     print("sunday")
else :
    print("Please enter weekday number between")
'''







#Q7 vowel print
'''
y =input("Enter a character: ").lower()

if(y=='a' or y=='e' or y=='i' or  y=='o' or y=='u'):
    print("this is vowel")
else:
    print("this is not vowel")
 '''   





#Q8 Largest number find
'''
a=int(input("enter your first:"))
b=int(input("enter your second:"))
c=int(input("enter your third:"))
 
if(a>b and a>c):
     print("a is greeater") 
elif(c>b and b>c):

    print("b is greater")
else:
    print("c is greater")

'''





