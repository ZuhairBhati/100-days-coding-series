# Write a program to express a number as a sum of two prime numbers


def isPrime(n):
    prime = True  #change made here
    if(n == 0 or n == 1):
        prime = False
    else:
        for i in range(2,n//2+1):
            if(n%i==0):
                prime = False
    
    return prime

def sum_of_two(n):
    for i in range(2,n//2+1):
        if(isPrime(i)):  #change made here
            if(isPrime(n-i)):
                return("{num1} is expressed as sum of {num2} and {num3}".format(num1=n,num2=i,num3=n-i))
        else:
            return"Can't be expressed as sum of primes"
n = int(input('Enter a Number: '))
print(sum_of_two(n))