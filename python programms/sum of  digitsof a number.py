#def get_sum(n):
    #sum=0
    #for digits in str(n):
        ##return sum
#n=int(input("enter the number"))
#print(get_sum(n))   
def get_sum(n):
    em=str(n)
    list_of_number=list(map(int,em.strip()))  
    return sum(list_of_number) 
n=int(input("enter the number"))
print(get_sum(n))     
