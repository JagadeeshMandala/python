#n=int(input("enter a number"))
#count=0
#while(n>0):
    #count=count+1
    #n=n//10
#print("the no.of digits are", count)  



#  another method
def countdigit(n):
    count=0
    while n!=0:
      n//=10
      count+=1
    return count
n=1234
print(countdigit(n))

