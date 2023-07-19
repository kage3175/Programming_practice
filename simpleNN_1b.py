'''import math

def sigmoid(x):
    return 1/(1+(math.e)**(-x))

def sigmoid_prime(x):
    return (math.e)**(-x)/((1+(math.e)**(-x))*(1+(math.e)**(-x)))

print(sigmoid_prime(2))'''

from sympy import *
import math

LR = 0.3 # Learning Rate

### initial
w1, w2, b1, b2 = -0.833770513732446, 0.250251862562123, -0.478702394792302, -0.106664741967491

### free variables
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

learning_set_file=open('learning_set_SNN1.txt', 'r')
outfile = open('result_vars.txt', 'w')
learning_set = []
while True:
    line = learning_set_file.readline()
    if not line:
        break
    temp_set = list(line.split())
    temp_set[0], temp_set[1] = int(temp_set[0]), int(temp_set[1])
    learning_set.append(tuple(temp_set))

output_NN = sigmoid.subs(x, bias2 + omega2 * sigmoid.subs(x, omega1 * input + bias1))
error = (output_NN - e_output) ** 2
d_error_w1, d_error_w2, d_error_b1, d_error_b2 = Derivative(error, omega1).doit(), Derivative(error, omega2).doit(), Derivative(error, bias1).doit(), Derivative(error, bias2).doit()


cnt=0
'''for case in learning_set:
    cnt+=1
    input_case, output_case = case[0], case[1]
    val_d_error_w1, val_d_error_w2, val_d_error_b1, val_d_error_b2 = d_error_w1.subs([(omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2), (input, input_case), (e_output, output_case)]), d_error_w2.subs([(omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2), (input, input_case), (e_output, output_case)]), d_error_b1.subs([(omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2), (input, input_case), (e_output, output_case)]), d_error_b2.subs([(omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2), (input, input_case), (e_output, output_case)])
    #print(f'error: {error.subs([(input, input_case), (e_output, output_case), (omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2)])}')
    #print(f'dE/dw1: {val_d_error_w1}, dE/dw2: {val_d_error_w2}, dE/db1: {val_d_error_b1}, dE/db2: {val_d_error_b2}')

    w1 = w1 - val_d_error_w1 * LR
    w2 = w2 - val_d_error_w2 * LR
    b1 = b1 - val_d_error_b1 * LR
    b2 = b2 - val_d_error_b2 * LR

    print(f'{cnt}차 실행 결과\nw1: {w1}, new w2: {w2}, new b1: {b1}, new b2: {b2}')
    #print(f'new error: {error.subs([(input, input_case), (e_output, output_case), (omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2)])}')
print(f'{w1}, {w2}, {b1}, {b2}', file=outfile)'''

for i in range(100):
    val_output_NN = output_NN.subs([(omega1, w1), (omega2, w2), (bias1, b1), (bias2, b2), (input, i)])
    print(f'output for {i}: {val_output_NN}')
    if val_output_NN > 0.5:
        result = 'over 50'
    else:
        result = 'under 50'
    print(f'판단결과: {result}')

learning_set_file.close()
outfile.close()