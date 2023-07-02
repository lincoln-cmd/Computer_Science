# 상속
class cal():
    def plus(self, x , y):
        return x + y
    
class cal2(cal):
    def minus(self, x, y):
        return x - y
    def plus2(self, x, y):
        print(super().plus(x, y))
        
        
    
    
user = cal2()
print(user.plus(1, 2))
print(user.minus(21, 7))
print(user.plus2(11, 2))


# 추상 클래스
'''
 - 추상 클래스는 abc 모듈의 ABCMeta 클래스를 상속받아 만든다.
 이 때, 반드시 metaclass = 메타클래스이름 의 형태로 상속받는다.
 - 추상 클래스는 자신의 객체를 생성할 수 없다.
 - 추상 메소드라는 @abstractmethod 데코레이터를 사용하여 자신의
 하위객체에게 특정 메소드의 생성을 강제할 수 있다.
 - 추상 메소드는 이름만 존재하고 내용은 없다.
'''

from abc import *
class Abstract(metaclass = ABCMeta):
    @abstractmethod
    def method(self):
        pass
    
class test(Abstract):
    def method(self): # 상위 클래스인 Abstract()에서 @abstractmethod 데코레이터가 붙은 함수는 상속받는 하위 클래스에서 반드시 정의 되어야만 한다.    
        pass

user2 = test()


# isinstance
a = 3
print(isinstance(a, int))
print(isinstance(user2, test))
print(isinstance(user, test))