num = int(input('Enter a Number: '))
def getFactors(num):
    i = 1
    while i <= num:
        if (num % i == 0):
            print(i,end=', ')
        i = i + 1

getFactors(num)