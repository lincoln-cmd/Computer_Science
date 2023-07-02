'''
 'r': 읽기
 'w': 쓰기(이미 같은 경로에 파일이 존재하면 파일 내용을 지워버림)
 'a': 쓰기용으로 열기. 단, 'w'와는 달리 이미 같은 경로에 파일이 존재할 경우 내용 덧붙이기
 'x': 배타적 생성모드. 파일이 이미 존재하면 예외를 일으킴
 'rb': 바이트 어레이 읽기
 'wb': 바이트 어레이 쓰기
 
 
 유니코드:
     문지 집합 하나로 모든 문자를 표현할 수 있게 하는 것이 목적

 UTF:
     유니코드 변환 인코딩 형식
'''

'''
 경로:
     1. 절대 경로:
         - 파일의 경로를 루트(가장 기본이 되는 폴더)부터 직접 기재하는 방식

     2. 상대경로:
         - 파일의 경로를 현재 위치로부터 상대적으로 입력
         - ./: 현재 폴더를 의미. 생략해도 무방
         - ../: 상위 폴더를 의미

'''

f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello.txt', 'w')
#text = f.read()
#print(text)

#text2 = f.readlines()
#print(text2)

#text3 = f.readline()
#print(text3)
#text3 = f.readline()
#print(text3)
#text3 = f.readline()
#print(text3)

f.write('new line')

f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello.txt', 'a')

f.write('\nnew line2')

#f = open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello.txt', 'x')

f.write('\nnew line3')

f.close()


with open('C:\\Users\\dhkim\\.spyder-py3\\autosave\\test_package\\hello.txt') as f:
    for i in f:
        print(i)





