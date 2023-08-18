a = ['','one ','two ','three ','four ', 'five ','six ','seven ','eight ','nine ','ten ','eleven ','twelve ','thirteen ','fourteen ','fifteen ','sixteen ','seventeen ','eighteen ','nineteen '];
b = ['', '', 'twenty','thirty','forty','fifty', 'sixty','seventy','eighty','ninety'];
num=int(input("Enter the value:="))
if(num <= 19):
        print("words")
elif(num > 19 and num<100):
            show.innerHTML = b[num[0]] + " " +a[num[1]];
        
elif(num == 100 or num == 200 or num == 300 or num == 400 or num == 500 or num == 600 or num == 700 or num == 800 or num == 900):
            show.innerHTML = a[num[0]] + " Hundered " + a[num[1]] + a[num[2]];
        
elif(num>100 and num<=109 or num>200 and num<=209 or num>300 and num<=309 or num>400 and num<=409 or num>500 and num<=509 or num>600 and num<=609 or num>700 and num<=709 or num>800 and num<=809 or num>900 && num<=909){
            show.innerHTML = a[num[0]] + " Hundered and " + a[num[1]] + a[num[2]];
        

elif(num>109 and num<=119 or num>209 and num<=219 or num>309 and num<=319 or num>409 and num<=419 or num>509 and num<=519 or num>609 and num<=619 or num>709 and num<=719 or num>809 and num<=819 or num>909 && num<=919){
            show.innerHTML = a[num[0]] + " Hundered and " + a[num[1] + num[2]];
        
elif(num>=120 && num<=999)
            show.innerHTML = a[num[0]] + " Hundered and " + b[num[1]] +" " + a[num[2]];
        
elif (num == 1000)
            show.innerHTML = "One Thousand"
        
