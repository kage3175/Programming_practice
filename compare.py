import os
from datetime import datetime

now = datetime.now()

class files():
    def __init__(self):
        self.name = ''
        self.result_list = []
        self.onlyin = []
        self.difference = [] #[file_name, line_num, type, content] 형식. type 1은 문장이 다른 거, type 2는 반대편 result에는 없는 줄이 있는 거, type 3는 반대편 result에는 있는 줄이 없는 거
        self.valid_file_list = []
    def put_name(self, name_):
        self.name = name_
    def put_valid_file_list(self, file_name):
        self.valid_file_list.append(file_name)
    def put_onlyin(self, file_name):
        self.onlyin.append(file_name)
    def put_difference(self, file_name, line_num, type_diff, content):
        self.difference.append([file_name, line_num, type_diff, content])
    def get_notexist(self):
        return self.not_exist
    def get_name(self):
        return self.name
    def get_onlyin(self):
        return self.onlyin
    def get_difference(self):
        return self.difference
    def get_valid_file_list(self):
        return self.valid_file_list

files1, files2 = files(), files()
line_cnt = 0
flag_exist1 = False
flag_exist2 = False

print("result1에 담긴 파일들은 누구 파일입니까: ", end='')
files1.put_name(input().replace('\n', ''))
print("result2에 담긴 파일들은 누구 파일입니까: ", end='')
files2.put_name(input().replace('\n', ''))
outfile_name = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '_' + files1.get_name() + '_' + files2.get_name() + '.txt'
outfile = open('./log/' + outfile_name, 'a', encoding='UTF-8')
print(now.year, '년', now.month, '월', now.day, '일 실시한', files1.get_name(), '와(과)', files2.get_name(), '의 결과 차이입니다.\n\n', file=outfile)

flist_1 = os.listdir('./result1')
flist_2 = os.listdir('./result2')

#없는 파일 찾는 코드
for file1 in flist_1:
    if file1 not in flist_2:
        flag_exist1 = True
        files1.put_onlyin(file1)
    else:
        files1.put_valid_file_list(file1)

for file2 in flist_2:
    if file2 not in flist_1:
        flag_exist2 = True
        files2.put_onlyin(file2)
        
if flag_exist1 or flag_exist2:
    print('둘 중 한 사람에게만 있는 파일이 있습니다.\n', file=outfile)
    if flag_exist1:
        print(files1.get_name() + '에게는 ', end = '', file=outfile)
        for filex in files1.get_onlyin():
            print(filex + ', ', end='', file=outfile)
    if flag_exist2:
        print(files2.get_name() + '에게는 ', end = '', file=outfile)
        for filex in files2.get_onlyin():
            print(filex + ', ', file=outfile, end='')
    print('가 있습니다.\n', file=outfile)
        
#내용이 다른 파일 찾는 코드(result1을 기준으로, result2와 다른 부분)
for file_name in files1.get_valid_file_list():
    line_cnt = 0
    file_checking1 = open('./result1/'+file_name, 'r', encoding='UTF-8')
    file_checking2 = open('./result2/'+file_name, 'r', encoding='UTF-8')
    while True:
        line1 = file_checking1.readline()
        line1.replace('\n', '')
        line2 = file_checking2.readline()
        line2.replace('\n', '')
        line_cnt+=1
        if not line2:
            if not line1:
                break
            else:
                files1.put_difference(file_name, line_cnt,2,line1)
                files2.put_difference(file_name, line_cnt,3,line1)
                while True:
                    line1 = file_checking1.readline()
                    line1.replace('\n', '')
                    if not line1:
                        break
                    line_cnt+=1
                    files1.put_difference(file_name, line_cnt,2,line1)
                    files2.put_difference(file_name, line_cnt,3,line1)
        elif not line1:
            if not line2:
                break
            else:
                files2.put_difference(file_name, line_cnt,2,line2)
                files1.put_difference(file_name, line_cnt,3,line2)
                while True:
                    line2 = file_checking2.readline()
                    line2.replace('\n', '')
                    if not line2:
                        break
                    line_cnt+=1
                    files2.put_difference(file_name, line_cnt,2,line2)
                    files1.put_difference(file_name, line_cnt,3,line2)
        elif line1 != line2 :
            files1.put_difference(file_name, line_cnt, 1, line1)
            files2.put_difference(file_name, line_cnt, 1, line2)
        else:
            continue
    file_checking1.close()
    file_checking2.close()

diff = files1.get_difference()
diff2 = files2.get_difference()
print(diff)
## result1에는 있는데 2에는 없는거 출력해야함

for x in range(len(diff)):
    print('===================================', file=outfile)
    if diff[x][2] == 1:
        print("In result of " + files1.get_name() + ', file ' + diff[x][0] + ', line ' + str(diff[x][1]) + ':\n' + diff[x][3] + '\n', file=outfile)
        print('But in result of ' + files2.get_name() + ':\n' + diff2[x][3] + '\n', file=outfile)
    elif diff[x][2] == 2:
        print('There is\n' + diff[x][3], file=outfile)
        print('in line ' + str(diff[x][1]) + ' of ' + files1.get_name() + ', but not in result file of ' + files2.get_name() + '\n', file=outfile)
    elif diff[x][2] == 3:
        print('There is\n' + diff2[x][3], file=outfile)
        print('in file '+ diff[x][0] +' in line ' + str(diff2[x][1]) + ' of ' + files2.get_name() + ', but not in result file of ' + files1.get_name() + '\n', file=outfile)
    else:
        print('something wrong!\n')
        
outfile.close()