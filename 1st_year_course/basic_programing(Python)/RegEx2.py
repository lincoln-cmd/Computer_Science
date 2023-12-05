import re

'''
# 실습1
p = re.compile('a.b')
re.match(p, 'a\nb')
p.match('a\nb')

a = p.match('akb')
b = p.match('aaabbb')
c = p.match('a\nb')
d = p.match('a.b')

print(a)
print(b)
print(c)
print(d)

p = re.compile('a.b', re.DOTALL) # \n도 매치되도록 함.

a = p.match('akb')
b = p.match('aaabbb')
c = p.match('a\nb')
d = p.match('a.b')

print(a)
print(b)
print(c)
print(d)


p = re.compile('a[\s\S]b') # 모든 문자와 매치

a = p.match('akb')
b = p.match('aaabbb')
c = p.match('a\nb')
d = p.match('a.b')

print(a)
print(b)
print(c)
print(d)
'''


'''
# 실습2
p = re.compile('a[.]{3,}') # 점(.)이 3개 이상만 매치

print(p.match('acccb'))
print(p.match('a...b'))
print(p.match('a.......b'))
print(p.match('a....'))



p = re.compile('[a-z]+') # 영어 소문자 여러개

m = p.search('123 python')
print(m.start() + m.end())

print(m.start()) # pattern에 맞는 첫번째 인덱스
print(m.end()) # pattern에 맞는 마지막 인덱스

print(p.search('123 python'))

print(m.group()) # 매치되는 부분을 직접 출력
'''

"""
# 실습3
data = '''
park 010-1234-5678
kim 010-3456-1234'''

p = re.compile('(\w+)\s(\d+[-]\d+)[-](\d+)')
print(p.match('park 010-1234-5678'))
# 여기서 compile 안의 소괄호는 각각 그룹으로 지정된다.
# (\w+)는 group 1, (\d+ [-] \d+)는 group2, 그리고 (\d+)는 group3.
# 그리고 각 그룹은 \g<group number>를 사용해서 불러올 수 있다.
print(p.sub('\g<2>-**** \g<1>', data))

m = p.search(data)
print(m.group(1))
"""

'''
# 실습4

p = re.compile('[a-zA-Z]\w*')
m = p.search('123 abc 456 def') # 조건에 맞는 단어 하나
print(m.group())

m = p.findall('123 abd 456 def') # 조건에 맞는 모든 단어를 리스트화
print(m)


p = re.compile('the')
print(p.findall('The cat was hungry. He was scared because of the cat'))
p = re.compile('the', re.I) # re.I : Ignore. 대소문자 구분 안함.
print(p.findall('The cat was hungry. He was scared because of the cat'))
'''


# 실습5

a = ['123', '123456789', '010-1234-5678', '1545648-4545445', '010-1111-2222', '010-333-33']

p = re.compile('^(\d+){3}[-](\d+){4}[-](\d+){4}$')
result = []

for i in a:
    p = re.compile('(\d{3})[-](\d{4})[-](\d{4})')
    if p.match(i):
        result.append(p.sub('\g<1>-\g<2>-****', i))

print(result)




