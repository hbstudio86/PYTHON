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
