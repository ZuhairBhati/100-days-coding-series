month = int(input("Enter the Month: "))
year = int(input("Enter the Year: "))

if (month == 1 or month == 3 or month == 5 or  month == 7 or month == 8 or month == 10 or month == 12):
    print('31')
elif (month == 2 and ((year % 4 ==0) or ((year % 4 == 0) and (year % 100 != 0)))):
    print('29')
elif (month == 2):
    print('28')
else:
    print('30')
