
def compute_hcf(x,y):

   if x>y:
       smaller=x
   else:
       smaller=x
   for i in range(1,smaller+1):
       if((x%i==0) and (y%i==0)):
           hcf=i
   return hcf
num1=int(input("enter the first number"))  
num2=int(input("enter the second number"))      
print("THe H.C.F is",compute_hcf(num1,num2))          

