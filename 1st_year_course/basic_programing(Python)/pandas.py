'''
 pandas
 
 - Numpy 기반으로 개발된 데이터 분석 도구.
 - pandas.Series는 1차원 데이터를 다루는 데 효과적이고,
 pandas.DataFrame은 2차원 데이터를 다루는데 유용.
 
'''

import pandas as pd
a = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns = ['col1', 'col2', 'col3', 'col4'], index = ['a', 'b'])

b = pd.DataFrame({'col1' : [1, 2, 3, 4], 'col2' : [5, 6, 7, 8]})

print(a.col1)
print(b['col1'])

print(a[:1]) # 인덱싱 x, 슬라이싱만 가능
print(b.iloc[0])

a['col5'] = [10, 11] # 새로운 열 추가
print(a)
a['col5'] = a['col5'] * 10 # 기존 열의 값을 변경
print(a)

del a['col2']
print(a)

print(a.apply(sum)) # defalut axis = 0, 열 방향
print(a.apply(sum, axis = 1)) # axis = 1: 행 방향

print(a)
print(a.apply(lambda x: x[0]**2, axis = 0))
print(a.apply(lambda x: x[0] + x[1], axis = 0))
print(a.apply(lambda x: x**2)) # 그냥 apply는 특정 방향을 가지고 함수 적용
print(a.applymap(lambda x: x**2)) # 각각 요소별로 함수 적용




'''
 isnull(): NaN이나, None인 경우 True, 그 외엔 False
 notnull(): isnull()의 반대
 dropna(): NaN이나 None을 소유한 행을 제외
 fillna(): NaN이나 None을 특정 수로 채울 수 있음
'''

a['col1'][0] = None
#a.col5[1] = None
#a['col5']['b'] = None
print(a)

print(pd.isnull(a))
print(a.dropna())
print(a.fillna('k'))




'''
 groupby method

 df.groupby('column name').agg(function) : 컬럼이름이 같은 것들끼리 함수 적용
'''

c = pd.DataFrame([['A', 30], ['B', 20], ['A', 50], ['B', 80]], columns = ['class', 'score'], index = ['Ana', 'Kal', 'Marry', 'Mike'])

print(c)
print(c.groupby('class').mean())
print(c.groupby('class').agg(lambda x: sum(x) ** 2))


