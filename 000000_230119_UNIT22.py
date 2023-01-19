## UNIT22 리스트와 튜플 응용하기 ##

# 1. 리스트 조작하기

#append 추가
#extend 확장
#insert 추가

#>> append 리스트 끝에 하나 추가

a = [1,2,3]
print(a)
a.append(100)
print(a)

a.append([10,11])   #리스트 안에 리스트 추가하기... 이건 뭘로 해석해야 하나...
print(a)


#>> extend 리스트 확장하기

a.extend([99,98])   # 여러개의 리스트를 추가 할 때 유용할 듯
print(a)


#>> insert 원하는 인덱스에 추가하기
a.insert(4,30)
print(a)
