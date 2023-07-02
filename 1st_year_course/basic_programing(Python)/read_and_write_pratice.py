'''
import os

dir_list = os.listdir("./") # 현재 디렉토리의 하위 디렉토리를 반환
for name in dir_list:
    print(name)
    
    
# 디렉토리 생성
os.mkdir('test')

'''

'''
실습1
file = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello2.txt', 'w', encoding = 'utf-8')
file.write('Hello python\n')
file.write('안녕하세요.\n')
lines = ['hi\n', 'hello\n', 'hola\n']
lines2 = ['oh\n', 'my\n', 'god\n']
file.write('\n'.join(lines)) # \n이 포함되지 않았을 때
file.writelines(lines2) # join을 사용히지 않았을 때
file.write(''.join(lines2)) # \n이 포함되었을 때
file.close()
'''


###################################################################


'''
#실습2
test1 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello2.txt', 'r', encoding='utf-8')
for line in test1:
    print(line)
test1.close()
test2 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello2.txt', 'r', encoding = 'utf-8')
content = test2.read()
print(content)
test2.close()
test3 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello2.txt', 'r', encoding = 'utf-8')
lines = test3.readlines()
print(lines)
test3.close()
'''


###################################################################


'''
#실습3
l1 = ['허걱', '허각', '허공']
l2 = ['\n구렁이', '\n팔렁이', '\n칠렁이']
l3 = ['\n구렁이', '\n구렁삼', '\n구렁사']
file = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello3.txt', 'w', encoding = 'utf-8')
file.write('금요일\n'); file.write('오후 4시 40분\n');
file.write('\n'.join(l1))
file.writelines(l2)
file.write(''.join(l3))
file.close()
'''


###################################################################

'''
#실습4
file1 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello3.txt', 'r', encoding = 'utf-8')

for line in file1: # 한 줄씩 읽어서 처리
    print(line, end = '')
    
file1.close()
print('---------')

file2 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello3.txt', 'r', encoding = 'utf-8')
content = file2.read() # 전부 읽기
print(content)
file2.close()
print('==========')

file3 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello3.txt', 'r', encoding = 'utf-8')
lines = file3.readlines()
print(lines)
file3.close()
'''

###################################################################


'''
#실습5
f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\add1.txt', 'w', encoding = 'utf-8')
f.write('good')
f.close()

# 기존 데이터를 지우고 새로 쓰기
f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\add1.txt', 'w', encoding = 'utf-8')
f.write('great!!!!')
f.close()

# 기존 데이터에 내용 추가
f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\add1.txt', 'a', encoding = 'utf-8')
f.write('\ngob!!!')
f.close()

f1 = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\add1.txt', 'a', encoding = 'utf-8')
for i in range(1, 11):
    f1.write('\n{}개 추가했습니다.'.format(i))
f1.close()
'''


###################################################################


'''
# 실습6
# 바이트로 저장
f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\byte_test.txt', 'wb')
f.write('안녕하세요. hi, hello. hola!'.encode())
f.close()

f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\byte_test.txt', 'rb')
d = f.read()
# binary파일을 읽을 때는 반드시 decode해야 함.
print(d.decode())
f.close()

print('바이바이~'.encode('utf-8'))
print(b'\xeb\xb0\x94\xec\x9d\xb4\xeb\xb0\x94\xec\x9d\xb4~'.decode())
'''


###################################################################


'''
# 실습7
with open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\t1.txt', 'w') as f:
    print('hi', file = f)
    print('hello', file = f)
    print('python', file = f)

with open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\t1.txt', 'r') as f:
    print(f.read())
'''


###################################################################


'''
# 실습8
import os

curlist = os.listdir('./')
for name in curlist:
    print(name)
    
os.mkdir('read_and_write_test_dir')
'''


###################################################################



# 실습9
# pickle 실습
import pickle

class Person:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        
p1 = Person(1, '철수'); p2 = Person(2, '영희')
li = [p1, p2]
# pickle은 byte 단위로 데이터를 저장할 때 사용.
with open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\person_byte.txt', 'wb') as f:
    pickle.dump(li, f)
    
with open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\person_byte.txt', 'rb') as f:
    content = pickle.load(f)
    print(content)
    print(type(content))
    for i in content:
        print(type(i))
        print(i.num, i.name)
        
print(content[0])
print(content[0].num)