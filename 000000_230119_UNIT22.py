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

#pop    지정 인덱스 삭제 (혹은 마지막)
#remove 값을 찾아서 삭제

a.pop() #이때 삭제한 요소를 반환 함
print(a)

a.pop(2)    #지정한 인덱스의 값을 삭제 한다.
print(a)

a.remove(100)   # 설정한 값을 찾아서 삭제 합니다.
print(a)

a.extend([100,100,100,100])   # 만약 여러개의 동일한 값이 있다면... 제일 처음의 값만 삭제 합니다.
print(a)
a.remove(100)
print(a)

# index 특정 값을 찾아 해당 index번호를 반환 함

print(a.index(99))

# count 리스트에서 해당 값의 개수를 구함

print(a.count(100))

# reverse 리스트의 순서 뒤집기

a.reverse()
print(a)

# sort 정렬하기
# sort(reverse = false)는 오름차순 / true 는 내림차수
# 같은 타입의 자료형만 정렬이 가능하다.

b = [4,67,2,8,73,54,21,1,15,99,61,43,32]

print("정렬전: ", b)
b.sort(reverse = False)
print('\t정렬(오름): ', b)
b.sort(reverse = True)
print("\t정렬(내림): ", b)

#>> sorted라는 함수는 정렬하여 새로운 리스트를 생성한다.

c = [4,67,2,8,73,54,21,1,15,99,61,43,32]

print("정렬전: ", c)

d = sorted(c)

print("정렬후: c =", c , "\n\td = ", d)


# clear 리스트의 모든 요소 삭제 하기

print(d)
d.clear()
print(d)
