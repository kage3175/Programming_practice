import os

class files():
    def __init__(self):
        self.name = ''
        self.result_list = []
        self.not_exist = []
        self.difference = {}
        self.valid_file_list = []
    def put_name(self, name_):
        self.name = name_
    def put_valid_file_list(self, file_name):
        self.valid_file_list.append(file_name)
    def put_notexist(self, file_name):
        self.not_exist.append(file_name)
    def get_notexist(self):
        return self.not_exist
    def get_name(self):
        return self.name
    def get_difference(self):
        return self.difference
    def get_valid_file_list(self):
        return self.valid_file_list

files1, files2 = files(), files()

print("result1에 담긴 파일들은 누구 파일입니까: ", end='')
files1.put_name(input().replace('\n', ''))
print("result2에 담긴 파일들은 누구 파일입니까: ", end='')
files2.put_name(input().replace('\n', ''))


flist_1 = os.listdir('./result1')
flist_2 = os.listdir('./compare_result1')

#없는 파일 찾는 코드
for file1 in flist_1:
    if file1 not in flist_2:
        files1.put_name(file1)
    else:
        files1.put_valid_file_list(file1)

for file2 in flist_2:
    if file2 not in flist_1:
        files2.put_name(file2)
        
#내용이 다른 파일 찾는 코드(result1을 기준으로, result2와 다른 부분)
for file_name in files1.get_valid_file_list():
    
