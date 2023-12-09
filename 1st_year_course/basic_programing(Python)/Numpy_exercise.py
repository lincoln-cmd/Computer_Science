import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2],
              [3, 4]])

print(np.sum(a))
print(np.sum(a, keepdims = True)) # 차원 유지
print(np.sum(b, axis = 0)) # axis = 0 : 열 방향으로
print(np.sum(b, axis = 1)) # axis = 1 : 행 방향으로

c = np.array([[4, 5], 
              [7, 8]])

print(b + c) # 같은 위치의 요소끼리 계산. 차원이 맞지않으면 오류
print(b - c)
print(b * c)
print(b / c)

print(b * 3)

print(np.matmul(b, c)) # Matrix Multiplication. 행렬곱



# Numpy 계산 시간 비교
import datetime

li = range(1, 1000000)
li2 = []

start = datetime.datetime.now()
for i in li:
    li2.append(i * 2)
print(datetime.datetime.now() - start)


arr = np.array(li)
start2 = datetime.datetime.now()
arr2 = arr * 2
print(datetime.datetime.now() - start2)


# np.concatenate()
print(np.concatenate((b, c), axis = 0))
print(np.concatenate((b, c), axis = 1))








