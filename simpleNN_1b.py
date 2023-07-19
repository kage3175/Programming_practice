'''import math

def sigmoid(x):
    return 1/(1+(math.e)**(-x))

def sigmoid_prime(x):
    return (math.e)**(-x)/((1+(math.e)**(-x))*(1+(math.e)**(-x)))

print(sigmoid_prime(2))'''

from sympy import *
import math

w1=1
w2=1
b1=1
b2=1

x = symbols('x')
sigmoid = 1/(1+(math.e)**(-x))
d_sigmoid = ((math.e)**(-x)) / ((1+(math.e)**(-x)))**2
e_output = symbols('e_o')
output = symbols('o')
input = symbols('i')
omega1 = symbols('ww11')
omega2 = symbols('ww22')
bias1 = symbols('bb11')
bias2 = symbols('bb22')

error = (sigmoid.subs(x, bias2 + omega1 * sigmoid.subs(x, omega1 * input + bias1)) - e_output) ** 2
d_error_w1 = Derivative(error, omega1).doit()
print(error)
print(d_error_w1)


#print(d_sigmoid.subs(x, 2))