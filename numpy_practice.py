import numpy as np

a=[[1,2,3], [4,5,6]]
b=np.array(a)
c=np.full((3,2), 1)

d=np.dot(b,c)

print(d)