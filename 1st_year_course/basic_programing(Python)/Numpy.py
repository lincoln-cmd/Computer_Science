'''
 - What is the Numpy?
 C언어를 기반으로 작성된 라이브러리. Numerical Python의 줄임말.
 파이썬에서 과학적 계산을 위한 핵심 라이브러리.
 다차원 배열 객체와 이들의 계산을 위한 다양한 도구 제공.
'''


'''
 배열(ndarray): 다차원 배열객체
 - np에서의 각 위치의 자료는 모두 같은 자료형이어야 한다.
 - np.array(컬렉션)을 통해 생성할 수 있다.
 - .dtype을 통해 각 데이터의 자료형을 알 수 있다.
 - linkedList는 리스트 공간을 미리 할당할 필요가 없지만, array는 미리
 공간을 할당해야 하고, 모두 같은 형태를 가져야 한다.
'''


import numpy as np

np.array([1, 2, 3, 4])
np.empty(10).dtype
print(np.array([1, 2, 3]).dtype)

data = np.array([1, 2, 3], dtype = np.float32) # 데이터 형태를 강제 설정 가능

#print(data.dtype)
#print(data)


'''
 배열과 리스트이 차이점
 1. 배열의 모든 원소가 같은 자료형이다.
 2. 배열의 원소 개수를 바꿀 수 없다.
 3. 파이썬은 자체적으로 배열 자료형을 제공하지 않기 때문에 numpy를 통해서만 사용할 수 있다.
 4. C언어로 구현되었기 때문에 파이썬 반복문에 비해 월등히 속도가 빠르며, vectorized operation을
 이용하여 간단한 코드로도 복잡한 선형 대수 연산을 빠르게 수행할 수 있다.
 5. Numpy 배열은 다차원으로 구성될 수 있고, .shape을 통해 몇 차원인지, 각 차원은 몇개의 원소로
 구성되어 있는지 확인할 수 있다.
'''


#print(np.array([1, 2, 3, 4]).shape) # (4,)
#print(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]).shape) # (4, 2)
#print(np.array([[1, 1, 1, 1], [2, 2, 2, 2]]).shape) # (2, 4)


'''
 - 특수 행렬 생성
 
 np.zeros(): 각각 0으로 채워진 배열 생성
 np.ones(): 각각 1로 채원진 배열 생성
 np.eye() | np.diag(): 대각행렬 생성
 np.empty(): 크기만 지정해 두고 요소는 초기화 되지 않은 배열 생성.
 각각의 요소는 가비지 값이 채워져 있음.

'''


#print(np.eye(3, dtype = np.int64))
#print(np.zeros((3, 5, 1)))

a = np.empty((3, 2))
#print(a)

a[0] = 1.
a[2] = 3.

#print(a)

#print(a[[0, 2]]) # array의 특정 행들만 가져와서 행렬을 생성하거나 반환할 수 있다.

b = np.empty((3, 5))

for i in range(15):
    b[i//5][i%5] = i

# numpy array만의 특수한 인덱싱
print(b[[1, 2], [2, 4]]) # return: [7. 14.] -> 7. = (1, 2), 14. = (2, 4)

# numpy array는 list와는 다르게 슬리이싱을 할 경우 복제가 되지 않음.이는 그 배열의 주소값만을 가져오기 때문. 따라서, .copy()를 통해서 복제해야한다.



'''
 - 요소별 조건 판별
 
 ==: 특정 조건을 만족하는 배열의 모든 요소 선별
 !=: 특정 조건을 만족하지 않는 배열의 모든 요소 선별
 &(and): 여러 조건을 사용할 경우 &를 이용하여 선별
 |(or): 위와 같음.
'''


c = np.array([0, 1, 2, 3, 1, 1, 2, 3])

#print(c == 1)
#print(c[c == 1])

#print(c != 1)
#print(c[c != 1])

#print((c == 1) & (c == 2))

#print((c == 1) | (c == 2))

#print(c[np.array([True, True, False, False, True, True, False, False])])



'''
 유용한 함수와 메소드
 
  - flatten(): 다차원 배열을 1차원으로 펼친다.
  - transpose(): 행과 열을 변환
  - np.reshape(): 다차원 배열의 shape을 바꾼다.
  - np.random.random(): 난수를 발생시킨다.(random.random과 비슷하나 이는 numpy array를 반환)
  - np.hstack([a, b]): 두개의 배열을 수평으로 합친다.
  - np.vstack([a, b]): 두개의 배열을 수직으로 합친다.
'''


d = np.diag((1, 2, 3))
d = np.eye(3, dtype = np.int64)
#print(d)

# flatten()
#print(d.flatten())

# transpose()
e = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
#print(e.transpose())

# np.random.random()
f = np.random.random((2, 3))
#print(f)

# np.reshape()
#print(f.reshape(3, 2))

# np.hstack(), np.vstack()
a, b = np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])
print('a : \n', a)
print('b : \n', b)
print('hstack : \n', np.hstack([a, b]))
print('vstack : \n', np.vstack([a, b]))

'''
 Numpy의 통계함수
 
  - np.mean: 평균
  - np.var: 분산
  - np.std: 표준편차
  - np.max: 최댓값
  - np.min:최솟값
  - np.median: 중앙값
  - np.percentile(x, 25): 하위 25%에 해당하는 수
  - np.exp: 지수함수
  - np.sin, np.cos, np.tan: 삼각함수, 단위는 radian
  - np.abs: 절댓값
  - np.sqrt: 제곱근
  - np.sign: 부호
  - np.isnan: NaN(Not a Number) 포함 여부 확인
  - np.unique: 중복 제거
  - np.sort: 정렬
  
  * axis를 지정해줘서 행 또는 열을 기준으로 통계함수를 적용할 수 있음.
  
'''
















