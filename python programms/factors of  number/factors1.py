num=int(input("enter the number"))
factors=[]
for i in range(1,num+1):
    if num%i==0:
        factors.append(i)
print("factors of {0}={1}".format(num,factors))        



