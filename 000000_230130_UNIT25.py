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
