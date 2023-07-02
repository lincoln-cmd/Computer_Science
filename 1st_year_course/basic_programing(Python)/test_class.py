class human:
    count = 'this is count'
    
    def __init__(self, height, age):
        self.height = height
        self.age = age
        self.__age = 31
        
    def __del__(self):
        print('delete') # 클래스를 받는 객체를 삭제할 때 실행
        
        
    def how_old(self, var1, var2):
        print(self.age)
        print(var1)
        print(var2)
        self.new_var = 333
        
    def how_tall(self):
        print(self.height)
        print(self.new_var)
        
    @staticmethod
    def addition(x, y):
        return x + y
    
    @classmethod
    def cmethod(cls):
        print('this is a class mtehod')
        print(cls.count)
        
    @property
    def age_getter(self): # getter
        return self.__age

    @age_getter.setter
    def age_setter(self, value): #setter
        self.__age = value
    
        
sh = human(185, 15)

sh.how_old(3, 4)
sh.how_tall()
del sh

# 정적 메소드

'''
 @staticmethod 데코레이터로 수식:
     인스턴스를 생성하지 않고 클래스를 이용해서 직접 호출할 수 있는 메소드
     메소드 내에서 멤버 변수를 호출 할 수 없고, self 매개변수도 사용하지 않는다.
'''

human.addition(10, 11)


# 클래스 메소드
'''
 @classmethod 데코레이터로 수식:
     정적 메소드와 유사하지만, 첫 번째 변수로 클래스 객체가 전달되는 것이 다름.
     cls 매개변수 사용
'''
human.cmethod()


# private, public 변수
'''
 Private 멤버는 내부에서는 접근이 가능하지만 클래스 외부에서 접근이 안되는 멤버.
 Public 멤버는 클래스 외부에서 접근이 가능한 멤버
 
 Python의 경우 기본적으로 모든 멤버는 public
'''
sh = human(185, 15)
#sh.__age # 클래스 외부에서는 접근이 안되서 이렇게 쓰면 오류가 난다.
# 불러 올 때
sh.age_getter # private 변수를 가져올 때 쓰는게 getter
# setter는 private 변수를 변경할 때 사용
sh.age_setter = 36
sh.age_getter
