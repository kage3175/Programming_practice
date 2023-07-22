from sympy import *
import numpy as np
import math

# input 20개, output 2개

LR = 0.3 # Learning Rate
FST_LAYER_NUM = 20
BLOCK = 1


omega_1 = [[symbols('w1_'+str(i))] for i in range(FST_LAYER_NUM)]
omega_2 = [symbols('w2_'+str(i)) for i in range(FST_LAYER_NUM)]
w1 = [0 for i in range(FST_LAYER_NUM)]
w2 = [0 for i in range(FST_LAYER_NUM)]
bias_1 = [[symbols('b1')] for i in range(FST_LAYER_NUM)]
bias_2 = [symbols('b2')]
b_1 = 0
b_2 = 0
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

for_subs = zip(omega_1, w1)
sub_arr = []
for pair in for_subs:
    sub_arr.append((pair[0][0],pair[1]))
for_subs = zip(omega_2, w2)
for pair in for_subs:
    sub_arr.append(pair)
sub_arr.append((symbols('b1'), b_1))
sub_arr.append((symbols('b2'), b_2))

output_layer = output_layer.subs(sub_arr) #마지막 output에서 w랑 b를 다 값으로 바꾼 것. i는 아직 안 바뀜

print(output_layer)