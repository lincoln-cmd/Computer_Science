'''
 정규 표현식
'''

'''
 ex) 다음과 같이 문자들이 나열된 list가 있다.
['124', '124124124', '010-1234-5678', '13546', '010-7777-8888', '4544879']

 이 중에서 전화번호 형식을 갖춘 것들만 걸러서 찾고 싶다고 하자.
 이를 for문과 split 등을 통해 걸러낼 수 있지만, 문자의 형식이 복잡해지면 코드도 복잡해지는 문제가 생긴다.
 이 때 사용할 수 있는 것이 '정규표현식'이다.
'''

# for문과 split을 사용한 방법
test = ['124', '124124124', '010-1234-5678', '13546', '010-7777-8888', '4544879']

for i in test:
    j = i.split('-')
    
    if len(j) == 3:
        print(j)

'''
 정규식
 
  - 특정한 규칙을 가진 문자열의 집합을 표현할 때 사용하는 언어
  - 문자열에서 특정한 조건을 만족하는 경우를 걸러낼 때, 일반적인 조건문으로는 다소 복잡할 수도 있지만, 정규 표현식을 이용하면 매우 간단.
  - 파이썬에서만 쓰이는 것이 아닌 general한 방식의 언어이기 때문에 익혀두면 다른 언어에도 도움이 됨.
  - 파이썬에서 정규식을 re 모듈이 제공
'''


'''
 정규 표현식
 
 *: 0회 이상의 반복
 +: 1회 이상의 반복
 ?: 0이나 1회 반복
 {m}: m회 반복을 허용
 {m, n}: m회부터 n회까지 반복 허용
'''

import re

re.match('y{2, 3}t', 'pyyython')
#re.search('')


'''
 .: 줄바꿈 문자를 제외한 문자
 ^: 문자열의 시작과 매칭
 $: 끝나는 문자열
 []: 문자 집합을 의미. [abc]와 같이 사용해서 a, b, c 중 하나를 의미하거나 [a-z]라고 써서 a부터 z까지 중 하나를 의미
 |: 또는
'''

re.match('p.t', 'python')
re.match('^p', 'python')
re.match('n$', 'python')

re.match('p[abc]t', 'python')
re.match('p[a-z]t', 'python')
re.match('pxt|pyt', 'python')


'''
 \d: 모든 숫자
 \D: 숫자가 아닌 문자
 \s: 화이트 스페이스(빈칸)와 매칭
 \S: 화이트 스페이스가 아닌 문자와 매칭
 \w: 숫자 또는 문자
 \W: 숫자 또는 문자가 아닌 것
'''

re.match('\d', 'python3')
re.match('\D', 'python3')
re.match('\s', 'python 3')
re.match('\S', 'python 3')

re.match('[a-z][A-Z]+', 'PPyython3')

re.match('[py]{2, 3}', 'Pypypypython')


'''
 re 모듈
 
 - re는 정규 표현식을 이용한 문자열 매칭에 사용되는 파이썬 라이브러리이다.
 - re.compile(정규식 패턴 문자열): 정규식 패턴을 파이썬이 사용가능한 정규식
 객체로 컴파일 해줌. 이를 통해 객체가 된 정규식은 match()와 search() 등에 사용 가능.
 - re.search(정규식 패턴 문자열, 대상 문자열): re.compile()을 통해 객체로 변환된
 패턴이나, 정규식 패턴 문자열을 대상 문자열에서 찾는 역할을 한다.
 - re.match(정규 패턴 문자열, 대상 문자열): re.search()와 비슷하나, 문장 처음부터
 패턴과 일치하는 문자열만 검색한다.
 - re.findall(): search나 match는 패턴과 일치하는 첫번째 문자열만 반환하지만 이는
 모든 문자열을 리스트 형태로 반환한다.
 - re.sub(pattern, repl, string): string에서 pattern을 찾아 repl로 치환
 - re.split(pattern, string): pattern을 기준으로 문자열 분리
'''

a = re.compile('[py]{2, 3}')
re.search(a, 'pypypypython')
re.match(a, 'pypypypython')

re.sub('\d', 'x', 'python333')
re.sub('\D', 'x', 'python333')

re.split('-', '010-1234-5678')
re.split('-[0-9]{4}-', '010-1234-5678')


