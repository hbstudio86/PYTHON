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

#>> dictionary 표현식으로 반복문을 이용해 dictionary 만들기 : 문법이 눈에 와닿지는 않는다.

#
#
#        ┌-----┬--(키와 값이 할당)
#        |      |        |     |
#        v      v        |     |
dic4 = {key : value for key, value in dict.fromkeys(key_list).items()}
#                        ^     ^         fromkeys로 key가 생성 -> key와 value를
#                        |     |                                      |
#                        └----┴--------------(여기로 입력)------------┘
#
#
print(dic4)

#>> key와 value를 반대로 
dic5 = {value2 : key2 for key2, value2 in dict.fromkeys(key_list).items()}
print(dic5) #이건 none : 'golf" 밖에 출력하지 못함 : 이건 키가 모두 동일해서 덮어 쓰인거다

#>> value에 강제로 값 할당

dic6 = {key : 0 for key, value in dict.fromkeys(key_list).items()}
print(dic6)

l9 = [1,2,3,None,5,6,7]
for kkk in l9:
    print(kkk)

#>> 디셔너리는 del로 삭제 하지 못한다. 오직 pop으로 키만 찾아 삭제가 가능하다.
#>> 그럼 값을 보고 삭제 하려면 어떤 방식을 사용해야 하는가?
#>> 위의 디셔너리 표현식으로 작성하되 if문으로 배제할 값을 빼고 출력하면 된다.

dic10 = {'alpha':10,'beta':20,'charli':30,'delta':40,'echo':50}
print(dic10)
dic10 = {key : value for key, value in dic10.items() if value != 20}
print(dic10)

# 6. Dictionary 내의 Dictionary

dic11 = {'A':{'A-1':30,'A-2':35},'B':{'B-1':11,'B-2':{'B-2-a':12.3,'B-2-b':12.8}}}
print(dic11,dic11['A']['A-2'],dic11['B']['B-1'],dic11['B']['B-2']['B-2-a'],sep='\n')

# 7. Dictionary의 복사

#>> 동일하게 대상이 지정이 되지 복사는 이루어지지 않는다

dic12 = dic10
print("dic12 is dic10 =",dic12 is dic10)
print("dic10 = ",dic10)
print("dic12 = ",dic12)
dic10['bata'] = 80
print("dic10 = ",dic10)
print("dic12 = ",dic12)

#>> dictionary는 copy로 복사가 된다.

dic13 = dic10.copy()
print("dic13 is dic10 =",dic13 is dic10)
print("dic10 = ",dic10)
print("dic13 = ",dic13)
dic10['beta'] = 99
print("dic10 = ",dic10)
print("dic13 = ",dic13)

#>> 중첩 dictionary는 copy로 복사가 되지 않는다.
#>> deepcopy로 복사가 이루어진다.

import copy

dic14 = dic11.copy()
print("dic11 is dic14=",dic11 is dic14)
print("dic11:",dic11)
print("dic14:",dic14)
dic11['B']['B-1'] = 100
print("dic11:",dic11)
print("dic14:",dic14)
dic15 = copy.deepcopy(dic11)
print("dic11 is dic15=",dic11 is dic15)
print("dic11:",dic11)
print("dic15:",dic15)
dic11['B']['B-1'] = 1100
print("dic11:",dic11)
print("dic15:",dic15)

print(dic10.values())

# 심사 문제 #

test_keys = ['alpha', 'bravo', 'charlie', 'delta']
test_value = [10, 20, 30, 40]

test_dic = dict(zip(test_keys, test_value))

test_dic = {key:value for key,value in test_dic.items() if key != 'delta' and value != 30}

print(test_dic)
