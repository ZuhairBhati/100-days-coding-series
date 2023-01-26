def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num = int(input('Enter a Number: '))
if num <= 0:
    print('Invalid')
else:
    for i in range(num):
        print(fibonacciSeries(i), end=' ')
