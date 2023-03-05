# UNIT 35 Class 속성과 정적, 클래스 메서드 사용하기 #

# 1. Class 속성 하용하기

class Person:
    bag = []    # 빈 리스트 형성 (속성)

    def put_bag(self,stuff):
        self.bag.append(stuff)
        
jack = Person()
tom = Person()

jack.put_bag('열쇠')
print(jack.bag)

tom.put_bag('자물쇠')
print(tom.bag)

#>> 여기서 클래스의 속성은 C++에서 static 멤버 변수와 비슷해 보인다.
#   값을 공유 한다.

#>> 만약 공유하고 싶지 않다면 생성자(__init__)로 속성을 부여 하면 된다.

class People:
    def __init__(self):
        self.bag = []
    def put_bag(self,stuff):
        self.bag.append(stuff)

tomas = People()
khan = People()

tomas.put_bag("열쇠")
khan.put_bag("자물쇠")

print(tomas.bag)
print(khan.bag)


# 위의 속성을 클래스 속성이라 하며, 아래의 속성을 인스턴스 속성이라 한다.

# 2. 비공개 Class 속성 사용하기

#>> 앞서 배운 것과 같이 외부의 접근을 제한하고자 한다면,  __속성을 사용하라

class Human:
    '''Human Class'''
    __age = 0

    def add_age(self,age = 1):
        '''Age added'''
        self.__age = age

    def show_age(self):
        '''Show age'''
        print("나이는",self.__age)

john = Human()

john.show_age()
john.add_age()
john.show_age()

# __doc__

print(john.__doc__)
print(john.add_age.__doc__)
print(john.show_age.__doc__)


# 3. 정적 메서드 사용하기

#>> 인스턴스를 사용하지 않고 메서드를 사용할 수가 있다.
#   @staticmethod : 역기서 @는 데코레이터라고 한다.
#   정적 메서드의 경우, 객체 내부의 필드 값을 손상 시키지 않고 원하는 결과를 얻기 위해 사용한다. 그래? 내가 제대로 이해 한게 맞나?

class Humanoid:
    __arr1 = [] # list

    def __init__(self):
        self.__arr1 = [1,2,3,4]
        print('set',self.__arr1)

    def add_num(self,num):
        self.__arr1.append(num)
        print('Add',self.__arr1)

    @staticmethod
    def sum_num(a,b):
        return a+b

key = Humanoid()

print(Humanoid.sum_num(1,2))    # 이게 왜 필요한거야?

# 4. 클래스 메서드 사용하기

# 이것이 내가 생각한 개념인것 같은데... 내부에 접근하는... 근데 왜필요 한거야?


# 심사 문제 #

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod
    def is_time_valid(time_string):    # 판별
        for i in list(map(int,time_string.split(":"))):
            if i > 24:
                return 0
            
    @classmethod
    def from_string(cls,str):
        cls.hour, cls.minute, cls.second = map(int,str.split(":"))  # 할당
        
        
 

 
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
