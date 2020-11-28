



num=int(input("enter the number"))
sum=0
temp=num
while(temp>0):
      fact=1




      rem=temp%10
      for i in range(1,rem+1):
          fact=fact*i
      print("factorial of %d=%d",(rem,fact))
      sum=sum+fact
      temp//=10
print("the factorial summation of the gi9ven number is:",(num,sum))
if(sum==num):
    print("The given number is a strong number")
else:
    print("The given number is a not astrong number")           