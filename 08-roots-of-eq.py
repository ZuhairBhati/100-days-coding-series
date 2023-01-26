import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if a == 0:
    print('Invalid')

d = b ** 2 - 4 * a * c
root = math.sqrt(abs(d))

if d > 0:
    print('Roots are Real')
    print((-b + root ) / (2 * a))
    print((-b - root ) / (2 * a))
elif d == 0:
    print('Roots are Equal')
    print(-b / (2 * a))
else:
    print('Roots are Unreal')
    print(-b / (2 * a), '+i', root)
    print(-b / (2 * a), '-i', root)