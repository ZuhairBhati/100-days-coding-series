# Write a program to Add two fractions

def addFractions(n1, n2):
    gcd = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

num1, den1 = map(int, list(input('Enter the Numerator and Denominator for first fraction: ').split(" ")))

num2, den2 = map(int, list(input('Enter the Numerator and Denominator for second fraction: ').split(" ")))   

lcm = (den1 * den2) // addFractions(den1, den2)

sum = (num1 * lcm // den1) + (num2 * lcm // den2)

num3 = sum // addFractions(sum, lcm)

lcm = lcm // addFractions(sum, lcm)

print(num3, '/', lcm)