## UHIT8 불과 비교 논리 연산자 알아보기  ##
#Python에는 == 와 != 비교 연산자 외
#is 와 is not 이 있다. 이것은 객체를 비교 하는 것이다
print(1==1) #이러면 두 값을 비교 한다
print(1==1.0) #역시 두 값을 비교 하므로 참이다
print(1 is 1.0) # 1이라는 객체와 1.0이라는 객체는 다르므로 거짓이다
print("Object ID: ",id(1),"Object ID: ",id(1.0),sep="//")
#논리 연산자
#&&
print(True and True)
print(False and True)
#||
print(True or False)
print("True or False = ",True or False)
#!
print("not True: ",not True)
#논리 연산자의 우선순위는 not and or 순이다

