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
