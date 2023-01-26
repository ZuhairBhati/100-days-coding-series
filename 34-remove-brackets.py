# Write a Program to Remove brackets from an algebraic expression

expression = input('Enter a Expression: ')

brackets = ["(",")"]
new_expr = ''

for i in expression:
    if i not in brackets:
        new_expr = new_expr + i
print(new_expr)