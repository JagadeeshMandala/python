n=int(input("enter a number"))
rev=0
while(n>0):



    digit=n%10
    rev=rev*10+digit
    n//=10
print("the revrsed ",rev)



