num=int(input("enter the number"))
rev=0
temp=num
while(num>0):


  digit=num%10
  rev=rev*10+digit
  num=num//10
if(temp==rev):
    print("IT is palindrome")

else:
    print("not palindrome")

