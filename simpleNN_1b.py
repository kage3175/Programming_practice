import math

def sigmoid(x):
    return 1/(1+(math.e)**(-x))

def sigmoid_prime(x):
    return (math.e)**(-x)/((1+(math.e)**(-x))*(1+(math.e)**(-x)))

print(sigmoid_prime(2))