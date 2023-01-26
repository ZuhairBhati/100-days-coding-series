num = int(input('Enter a Number: '))

def getFactorial(num):
    if num == 0:
        return 1
    else:
        return num * getFactorial(num - 1)
    
fact = getFactorial(num)
print(fact)