lower=int(input("enter the lower bound"))
upper=int(input("enter the upper bound"))
sum=0
for i in range(lower,upper+1):
    sum=sum+i
    i=i+1
print("the sum of all numbers",sum)    