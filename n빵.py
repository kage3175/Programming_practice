income={}
outcome={}

s=''
k=''
num_people=0

while s!='-1':
    s=input()
    k=input()
    if s=='-1' or k=='-1':
        break
    list_name=list(s.split())
    list_money=list(map(int, k.split()))
    i=0
    for name in list_name:
        try:
            income[name]+=list_money[i]
        except KeyError:
            income[name]=list_money[i]
            num_people+=1
        i+=1

sum_income=0

keys=income.keys()
for key in keys:
    sum_income+=income[key]

for key in keys:
    outcome[key]=income[key]-sum_income/num_people

keys=outcome.keys()
for key in keys:
    if outcome[key]>0:
        print(key,"은",outcome[key], "원을 받아야 합니다.")
    elif outcome[key]<0:
        print(key,"은",-outcome[key], "원을 내야 합니다.")
    else:
        continue
