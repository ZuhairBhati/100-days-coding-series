#  Body Mass Index

# You are given the height H (in metres) and mass M (in kilograms) of Anusree. The Body Mass Index (BMI) of a person is computed as M/H^2.

# Report the category into which Anusree falls, based on his BMI:

# Category 1: Underweight if BMI ≤18

# Category 2: Normal weight if BMI ∈{19, 20,…, 24}

# Category 3: Overweight if BMI ∈{25, 26,…, 29}

# Category 4: Obesity if BMI ≥30

# Input:

# The first line of input will contain an integer, T, which denotes the number of testcases. Then the testcases follow.

# Each testcase contains a single line of input, with two space separated integers, M,H, which denote the mass and height of Anusree respectively.

# Output:

# For each testcase, output in a single line, 1,2,3 or 4, based on the category in which Anusree falls.

test = int(input())

for i in range(test):
    w, h = list(map(int,input().split(' ')))
    bmi = int(w/(h**2))
    if bmi <= 18:
        print('1')
    elif bmi > 18 and bmi < 25:
        print('2')
    elif bmi >= 25 and bmi <=29:
        print('3')
    else:
        print('4')