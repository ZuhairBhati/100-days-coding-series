def quadrants(x ,y):
    if (x > 0 and y > 0):
        print('Points lies in First Quadrant')
    elif (x < 0 and y > 0):
        print('Points lies in Second Quadrant')
    elif (x < 0 and y < 0):
        print('Points lies in Third Quadrant')
    elif (x > 0 and y < 0):
        print('Points lies in Fourth Quadrant')
    else:
        print('Point lies at Origin')

x_cor = int(input('Enter x co-ordinate: '))
y_cor = int(input('Enter y co-ordinate: '))

quadrants(x_cor, y_cor)