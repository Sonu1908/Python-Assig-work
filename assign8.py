#Q1..that checks whether a passed string is palindrome or not.

a=input("Enter string : ")
b=a[-1::-1]
if(a==b):
    print("Palindrome")
else:
    print("Not palindrome")



#Q1....
def fun(a):
    c=list(a)
    b=list(a)
    b.reverse()
    #print(b)
    
    if(b==c):
        return "palindrom"
    else:
        return "not palindrom"


x=input("enter your name: ")
print(fun(x))








#Q2 Find Factors of Number (function)

def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320
factors(num)









#Q3Check whether a given year is a leap year or not

a=int(input("Enter a year:"))
def leapyear(a):
 if(a%400==0) and (a%100==0):
    ans="year is a leap"
 elif(a%4==0)and (a%100!=0):
    ans="year is a leap"
 else:
    ans="is not a leap year"
 return ans
z=leapyear(a)
print(z)







#Q4..Write a Pythagorean function in Python.

a=int(input("enter: "))
b=int(input("enter: "))
c=int(input("enter: "))
if(a**2 + b**2)==c**2:
    print("proved")
else:
    print("not proved")    



#Q5..Find the sum of digit of given number
'''
a="246"
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
'''






#factorial number
'''
def fact(a):
    if(a==0):
        return 1
    else:
        return ((a)*fact(a-1))
num=int(input("Enter a number: "))
result=fact(num)
print(result)
'''

