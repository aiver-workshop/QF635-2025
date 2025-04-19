"""
Debug your first Python application with breakpoints.

Learn the following techniques:
    - Set breakpoints
    - Step through program line by line
    - Select and evaluate an expression

"""

from numpy import log as ln

a = 5
b = 8
c = a + b
d = 5 * c
print('d is {}'.format(d))

n1 = ln(2)
print('ln(2) is {}'.format(n1))

print('ln(5) is {}'.format(ln(5)))

print('ln(2) + ln(5) is {}'.format(n1 + ln(5)))

print('ln(2 x 5) {}'.format(ln(2*5)))
