from sympy import *
import numpy as np
import math

# input 20개, output 2개

LR = 0.3 # Learning Rate
FST_LAYER_NUM = 20
BLOCK = 1


omega_1 = [[symbols('w1_'+str(i))] for i in range(FST_LAYER_NUM)]
omega_2 = [symbols('w2_'+str(i)) for i in range(FST_LAYER_NUM)]
bias_1 = [[symbols('b1')] for i in range(FST_LAYER_NUM)]
bias_2 = [symbols('b2')]
input = symbols('i')
output = symbols('o')

x = symbols('x')
sigmoid = 1/(1+(math.e)**(-x))

omega_1_arr = np.array(omega_1)
omega_2_arr = np.array(omega_2)
bias_1_arr = np.array(bias_1)
bias_2_arr = np.array(bias_2)
fst_layer = omega_1_arr.dot(input) + bias_1_arr
for i in range(fst_layer.size):
    fst_layer[i] = sigmoid.subs(x, fst_layer[i][0])
temp = omega_2_arr.dot(fst_layer) + bias_2_arr

output_layer = sigmoid.subs(x, temp[0])
print(output_layer)