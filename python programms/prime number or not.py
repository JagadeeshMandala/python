x=int(input("enter the number"))

if(x>1):
   for i in range(2,x):
       if(x%i)==0:
           print("not prime number")
           print(i ,"times", x//i,"is" ,x)
           break
   else:
       print("prime number")        

else:
    print("not prime number")