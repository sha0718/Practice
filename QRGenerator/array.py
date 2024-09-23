def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5 )+1):
        if n % i == 0:
            return False
    return True
num = int(input("enter ur number"))    
if is_prime(num):
    print(f"the {num} is prime")
else:
    print(f" the {num} is not prime")    


            


 






    
 









