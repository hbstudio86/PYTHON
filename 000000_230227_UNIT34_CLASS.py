# UNIT 34 CLASS #

# 1. Class 와 method 만들기

class Person:
    def greeting(self):
        print('hello')

class People:
    def greeting(self):
        print('HELLO')


#>> class를 선언 할 때 첫 글자는 대문자여야 한다.


james = Person()    # 인스턴스 = 클래스()
tom = People()
#>> 매서드 호출하기

james.greeting()
tom.greeting()
#>> python은 뭐든게 class로 되어 있다

#>> 인스턴스 특정 클래스의 인스턴스 인지 확인 하는 방법 : isinstance(instance, class) = return true or false
print(isinstance(tom,Person))

# 2. 속성 사용하기

class Test1:
    def __init__(self): # 초기화 할 때 할당한다.
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)

test1 = Test1()

test1.greeting()

# 여기서 self는 me, this 와 마찬가지로 호출하는 자기 자신을 의미한다.
# 그냥 me나 this를 쓰지 꼭~ 차별화 하고 싶어 한다...

# 3. 인스턴스 생성시 값을 받기


class Test2:
    def __init__(self,name,age,address):    # 생성자 느낌이 강하네
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print(f'{self.hello} 저는 {self.name}입니다.\n올해 {self.age}살이며,\n주소는 {self.address}에 살고 있습니다.')

test2 = Test2('쾌남',33,'충북 청주')
test2.greeting()

print(test2.name,test2.age)

# list unpacking도 가능하다.

class Test3:
    def __init__(self,*args):
        self.name = args[0]
        self.age = args[1]
    def greeting(self):
        print(f'name = {self.name}\nages = {self.age}')

test3 = Test3(*['Jack',38])
test3.greeting()

#>> 위의 생성자의 경우 외부 접근이 가능하다.

print(test3.name)

#>> data의 무결성을 위해서는 외부 접근의 제한이 필요로 하다
#   public과 private 개

class Test4:
    def __init__(self,name,age,address):
        self.__name = name
        self.__age = age
        self.__address = address

    def greeting(self):
        print(f'name = {self.__name} \nage = {self.__age}\naddress = {self.__address}')

test4 = Test4('TOM',12,'USA')

test4.greeting()

# 심사 문제 #

class Annie:
    def __init__(self,health,mana,ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        print('티버: 피해량',self.ability_power * 0.65 + 400)


health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
