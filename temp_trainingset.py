import random

outfile=open("learning_set_SNN1.txt", "a")

for i in range(1000):
    x = random.randint(1,101)
    if x > 50 :
        print(str(x)+" 1", file=outfile)
    else :
        print(str(x)+" 0", file=outfile)