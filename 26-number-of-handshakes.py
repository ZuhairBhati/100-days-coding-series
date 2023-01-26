#  Write a program to calculate Maximum number of handshakes

no_of_people = int(input('Enter Number of People: '))

no_of_handshakes = int(no_of_people * ((no_of_people - 1 )/ 2))

print(no_of_handshakes)