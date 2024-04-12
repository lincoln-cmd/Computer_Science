'''
 API란?

 - API(Application Programming Interface)는 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는
기능을 제어할 수 있게 만ㄷ는 인터페이스를 뜻한다. 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스를 제공한다.

 - 파이썬의 함수나 클래스 같은 기능들 하나하나가 일종의 API이다.

'''



'''
 Rest란?
 
 - Rest(Representational State Transfer)란 자원(Resource)의 표현(Representation)에 의한 정보 전달.
예를 들면, 파이썬의 list나 dictionary 등(자원)을 json 파일의 형태(표현)으로 전달하는 것.

 - Rest API란? Rest의 특징을 지키면서 API를 제공하는 것이다.

'''



'''
 Rest의 구성 요소

 자원(Resource): URI
 인터넷 주소와 같은 형식
 
 행위: HTTP 메소드
 GET / POST / PUT / DELETE
 
 표현: Representation of Resource
 JSON, XML, RSS 등

'''



################################################################################################
import requests

result = requests.get('https://map.naver.com/p/api/location/geocode?coords=127.87523260653347,35.12574448240886&orders=admcode,legalcode')

print(result)
print(result.json()) # dictionary 형태로 반환








