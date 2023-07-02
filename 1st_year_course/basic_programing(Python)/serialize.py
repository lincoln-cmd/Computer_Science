'''
 직렬화:
     - 객체를 연속적인 데이터로 변환하는 것. Serialize
     - 객체를 컴퓨터에 저장하기 위해서는 직렬화가 필요
'''


'''
 pickle 모듈 사용.
 
 pickle.dump(출력할 객체, 파일객체): 파일객체에 출력할 객체를 저장.
 
 with open('test.txt', 'wb') as f: 직렬화를 할 때는 바이트 어레이 쓰기인 wb 사용
     pickle.dump([1, 2, 3, 4], f)
     
     pickle.dumps(출력할 객체): 출력할 객체를 바이트 형태로 반환
     
     pickle.dumps([1, 2, 3, 4])
     
     pickle.load(파일객체): pickle을 통해 바이트화 되어 저장된 파일객체를 다시 원본의 모습으로 반환
     
     pickle.loads(바이트 객체): pickle을 통해 바이트화 된 객체를 다시 원본의 모습으로 반환
     
     pickle.loads(pickle.dumps([1, 2, 3, 4]))
'''

import pickle

pickle.dumps([1, 2, 3, 4])

pickle.loads(b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04e.')



'''
 Json은 pickle과는 다른 직렬화 방식으로, 서로 다른 언어로 작성된 프로그램에서 통신할 때 쓸 수도 있고,
 인간이 보기에 알아보기 편한 형식으로 저장할 수 있기 때문에 널리 사용. 단, json으로 직렬화 할 수 있는 객체는
 한정되어 있음. json은 범용화 직렬화 모듈.
 
 json.dumps([1, 2, 3, {'4':5, '6':7}])
  -> String 형식으로 반환
 
 json.loads('[1, 2, 3, {"4":5, "6":7}]')
  -> json화된 data를 list와 dictionary 등으로 복원
 
'''

import json
json.dumps({'a':1, 'b':2, 'c':3})

json.loads('{"a": 1, "b": 2, "c": 3}')


'''
 import json
 with open('test.txt', 'w') as f:
     json.dump([1, 2, 3, {'4':5, '6':7}])
      -> 파일에 json화된 객체를 저장
      
 with open('test.txt','r') as f:
     json.load(f)
      -> json화된 data를 list와 dictionary 등으로 복원
'''







