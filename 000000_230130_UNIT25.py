## UNIT25 Dictionary 활용하기 ##

# 1. key-value 추가하기
#>> setdefault, update

dic1 = {"a":1,"b":2}
print("원래 dic1의 값 :",dic1)

dic1.setdefault('c')
print("Default C의 결과",dic1)

dic1.setdefault('d',10) # c, 10으로 하면 수정이 되지 않은다.
print("Default D의 결과",dic1)

dic1.update(c=99)
print('update(c=99)의 결과',dic1)

#>> 복수의 형태도 가능하다
dic1.update(a=44,b=33)
print("a=44,b=33의 결과",dic1)

#>> 키 값이 숫자일 경우 update({})의 형태로 수정할 수 있다.
dic2 = {1:"하나",2:"두울"}
print("dic2의 기본 값:",dic2)

dic2.update({1:"ONE",2:"TWO",3:"THREE"})
print("dic2의 update 결과:",dic2)

# 2. Key값 삭제 하기

print("dic1의 값:",dic1)
dic1.pop("c")   # 삭제한 dictionary 값을 리턴한다.
print("dic1의 값(삭제후):",dic1)

#>> 삭제해야 할 key가 없다면 기본값을 리턴 하도록 되어 있다... 지정안했다면??

print("dic1에서 k를 삭제 했을때, 값 지정",dic1.pop('k',0))
#print("dic1에서 k를 삭제 했을때, 값 없음",dic1.pop('k'))  error를 띄운다.

#>> del dic[]의 형태로 삭제를 할 수도 있다.

del dic1['b']
print("del dic1[]의 형태를 사용했을 때",dic1)

#>> 임의 키-값을 삭제 하기... 이런게 왜 필요한것이지?

dic2.update({4:"FOUR",5:"FIVE"})
print("임의 삭제 전",dic2)
print(dic2.popitem())   # 임의로 삭제한 킥-값은 튜플로 출력 된다.
print("임의 삭제 후",dic2)

#>> 모든 키-값을 삭제 하는 것은 clear() 메서드를 이용한다.

# 3. 키-값 가져오기

print(dic2.get(1))  # 이거랑
print(dic2[3])      # 이거랑 무슨 차이? // 위의 형식이 더욱 복잡한데
print(dic2.get(8,0))    # 없은 키캆의 경우 0을 리턴하도록 한다.

#>> 모든 키-값을 가져오는 메서드

print(dic2.items())

#>> 모든 키를 가져오는 메서드

print(dic2.keys())

#>> 모든 값을 가져오는 메서드

print(dic2.values())

# 4. dictionary 만들기

key_list = ['alpha','beta','charli','delta','echo','fox','golf']
dic3 = dict.fromkeys(key_list)
print(dic3)

# 5. 반복문과 dictionary

for i in dic2:
    print(i,end='') # 이런 경우 값은 출력되지 않는다.

print()

for key, value in dic2.items(): # 이런 형태도 가능하다. for key, value in {'a':1,'b':2...}.items():
    print(key,value)

#>> key만, 값만 따로 받아 올 수 있다. 위에서 사용한 메서드인 keys(), values()가 그것이다.

for key in dic2.keys():
    print("key..",key)

for value in dic2.values():
    print("value..",value)
