"""
User a debugger to step through the following script that calculate sum of squares.

"""

a = 1
total = 0

while a <= 10:
    b = a * a
    total = total + b
    a = a + 1

print('total is {}'.format(total))