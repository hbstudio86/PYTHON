# UNIT 36 클래스 상속 사용하기 #

# 1. 기본적인 형태
#>>> class 기반클래스 이름:
#       코드

#>>> class 파생클래스 이름(기반클래스 이름):
#       코드

class Person:
    def cplint(self):
        print("안녕하세요")

class Student(Person):
    def study(self):
        print("공부하기")

james = Student()

james.study()
james.cplint()

# >> 상송관걔 확인하는 함수 issubclass(파생클래스, 기반클래스) => True False 형태로 출력한다.

# 2. 부모 클래스의 속성에 접근하기

class A:
    def __init__(self):
        print('A __init__')
        self.hello = '안녕하세요'
class Aa(A):
    def __init__(self):
        print('Aa __init__')
        super().__init__()  # 부모 클래스의 __init__ 메서드를 호출한다.
        self.school = '파이썬 코딩 도장'

tomas = Aa()
print(tomas.school)
print(tomas.hello)

# 3. 메서드 오버라이딩

class B:
    def greeting(self):
        print("Class B!!")

class Bb(B):
    def greeting(self):
        print("Class BB!!")

class Bbb(B):
    def greeting(self):
        super().greeting()  # 이런식으로 부모 클래스로부터 함수를 불러올 수 있다.
        print("BB")


CB1 = Bb()
CB1.greeting()

CB2 = Bbb()
CB2.greeting()

# 역시 오버라이딩이 가능하다.

# 4. 다중 상속

class CSuper1:
    def f1(self):
        print("CSUPER1")

class CSuper2:
    def f2(self):
        print("CSUPER2")

class CSub(CSuper1, CSuper2):
    def f3(self):
        print("CSUB")

csub1 = CSub()
csub1.f1()
csub1.f2()
csub1.f3()

# 5. 다이아몬드 상속

class CSuper3:
    pass

class CSuper4(CSuper3):
    pass

class CSuper5(CSuper3):
    pass

class CSuper6(CSuper4,CSuper5):
    pass

print(CSuper6.mro())    # 상속 우선순위를 표시 한다.

# 6. 추상 클래스

from abc import *

class CSuperABC(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod # 추상 메서드로 만들기 : 한마디로 메서드의 형태만 있다.
    def go_to_school(self):
        pass

class CSub2(CSuperABC):
    def study(self):
        print("공부하기")
    def go_to_school(self):
        print("학교에가기")

csub2 = CSub2()
csub2.study()
csub2.go_to_school()
