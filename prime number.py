
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
         if num % i == 0:
             return False
    return True
   
#Taken user input

n = int(input("enter a number: "))

if check_prime(n):
    print(n, "is a prime number")

else:
    print(n, "is not prime number") 

