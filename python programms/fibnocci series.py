nterms=int(input("enter how many terms"))
n1,n2=0,1
count=0
if nterms<=0:
    print("incorrect input")
elif nterms==1:
    print(n1)
else:
    print("fibnocci series :")
    while(count<nterms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1    
