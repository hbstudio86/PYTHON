## UNIT 26 SET ##

#>> set는 집합 개념이다

# 1. set 문법

set1 = {10,20,30}   # 중괄호를 쓴다
print(set1)

#>> set는 순서가 정의되어 있지 않다고 한다.

for i in range(10):
    print(set1)

#>> set는 리스트, 튜플, 딕셔너리와 다르게 인덱스로 접근을 할 수가 없다.

# 2. set 내용 확인

print("10이 있는가?",10 in set1)
print("15이 있는가?",15 in set1)
print("20이 있는가?",20 in set1)

# 3. set으로 set 만들기

set2 = set("Hello World!")  # 문자열의 경우 연속 데이터로 취급, 중복된 문자는 제외한다.
set3 = set(range(10))
set4 = set()                # 비어있는 set이 생성된다.

print(set2,set3,set4,sep='\n')

# 4. 집합연산 사용하기

set5 = {1,2,3,4}
set6 = {2,3,4,5}

print(set5|set6)    # or 연산자 |는 합집합
print(set.union(set5,set6))
print(set5&set6)    # and 연산자 &는 교집합
print(set.intersection(set5,set6))
print(set5-set6)    # - 연산자는 차집합
print(set.difference(set5,set6))
print(set5^set6)    # ^ 연산자는 대칭차집합
print(set.symmetric_difference(set5,set6))

# 5. 집합 연산 후 할당 연산자 사용

set5 |= {6}         # |=는 좌변값에 우변값을 추가 하는 것이다
set5.update({7})    # 위의 형식을 메서드로 표현함

print(set5)

set5 &= {1,3,5,7,9} # &=는 좌변값에 우변값의 일치하는 부분만 추가를 한다.
set5.intersection_update({1,3,4,5,7,8}) # 이 문법이 더 어렵네?
print(set5)

set5 -= {7}         # -=는 좌변값의 집합에서 우변값의 집합을 제거한다.
set5.difference_update({3})
print(set5)

set5 ^= set6        # ^=는 좌변값의 집합에 우변값과 겹치지 않는 값을 저장한다.
set5.symmetric_difference_update({11,12,13,14,15})
print(set5)

# 6. 부분집합, 진부분집합 여부 확인

set7 = {1,2,3,4,5}
set8 = {1,2,3,4,5}
set9 = {1,2,3,4,5,6}

print(set7<=set8)
print(set7>=set8)

print(set7>set9)
print(set7<set9)
