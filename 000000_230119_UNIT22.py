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

# 2. 리스트 할당 / 복사

#>> a = [...]의 경우 a는 리스트를 가리키고 있다고 이해하면 되겠다. 마치 포인터 처럼

aa = [1,2,3]    # aa는 [1,2,3]이라는 리스트를 가리키고 있다.
bb = aa         # bb에 aa를 할당하면 bb또한 aa가 가리키는 리스트를 가리키고 있는 것이다.
                # c++에서의 참조 변수랑 어찌보면 같다고 볼 수 있겠다. 원본을 가리킨다는 점이
print('aa: ', aa)
print('bb: ', bb)
print('aa is bb: ' , aa == bb)
print('aa is bb: ' , aa is bb)

aa[1] = 4       # 따라서 aa의 2번 index의 값을 변경하면 bb 또한 동일하다. (당연한거겠지만)

print('aa: ', aa)
print('bb: ', bb)
print('aa is bb: ' , aa is bb)  # shallow 복사가 이루어 진다

cc = aa.copy()  # copy 함수를 사용하면 deep 복사가 이루어 진다.

print('aa: ', aa)
print('cc: ', cc)
print('aa is cc: ' , aa is cc)

aa[1] = 9

print('aa: ', aa)
print('cc: ', cc)
print('aa is cc: ' , aa is cc)


# 3. 리스트와 반복문
i = 0
for x in cc:
    print("cc[",i,"] = ",x,sep="")  #C/C++ Style 과 비슷하게 해버렸다.
    i+=1

#>> index 번호와 리스트를 같이 출력하려면 아래와 같은 문법을 쓴다.

for index, value in enumerate(cc):
    print(index,value)

#>> 위의 형태를 좀 더 Python 스럽게 한다면...
for index,value in enumerate(a, start=1):   # index 시작 번호를 지정할 수 있다.
    print(index,value)


# 4. 작은 값, 큰 값 찾기

print(c)
print(min(c))
print(max(c))

# 5. 총 합계 구하기

print(sum(c))

# 6. 리스트 컴프리헨션

#>> 특정한 식을 리스트 내에서 선언할 수 있다.
#>> a = [i for i in range(10)] 이런식으로 말이다.

e = [i for i in range(10)]  # 뭔가 간단하지만 해석하기 힘들겠다.
print(e)

f = list(i for i in range(0,20,2))
print(f)

# if문도 넣을 수 있다.

g = [i for i in range(10) if i % 2 == 0]
print(g)

# 복잡한 형태의 반복문
#>> 뭔가 더러운 문법이 만들어 지는것 같다...

f = [ i * j for i in range(2,10)
      for j in range(1,10)]
print(f)

#>> 리스트의 내포의 동작 순서는 뒤에서 앞이다.

# 리스트 map사용하기

print("정수형 리스트 e의 내용\n",e)
e = list(map(float,e))
print("실수형으로 변경 후 e의 내용\n",e)
e = list(map(str,e))
print("문자열로 변경 후 e의 내용\n",e)


# 7. TUPLE이용하기

#>> TUPLE도 리스트와 마찬가지로 메서드를 사용할 수 있으나
#>> 값이 불변이기에 APPEND와 같은 항목을 추가하는 것은 불가하다

t1 = (1,2,3,4,5)    # t1 = tuple({1,2,3,4,5})
print("3의 index는?",t1.index(3))
print("1의 개수는?",t1.count(1))

t2 = tuple(i for i in range(20) if i % 3 == 0)  # 이 문법에서는 가능하고 위에서는 {}를 써줘야 한다.
print(t2)

print(t1[2])


# 심사 문제 #

num, exp = map(int,input().split())
t3 = [ 2 ** x for x in range(num,exp+1) if x != num + 1 and x != exp-1]
print(t3)
