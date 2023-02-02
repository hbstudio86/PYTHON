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
print(set5-set6)    # - 연산자는 차집합    : 기준 집합에서 대조 집합에 없는것
print(set.difference(set5,set6))
print(set5^set6)    # ^ 연산자는 대칭차집합 : 서로 없는것
print(set.symmetric_difference(set5,set6))

# 5. 집합 연산 후 할당 연산자 사용

set5 |= {6}         # |=는 좌변값에 우변값을 추가 하는 것이다
set5.update({7})    # 위의 형식을 메서드로 표현함

print(set5)

# 심사 문제 #
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

print(set7<=set8)   # 부분집합인지
print(set7>=set8)   # 상위집합인지

print(set7>set9)    # 진상위집합인지
print(set7<set9)    # 진부분집합인지

#>> 부등호로 해당 집합이 부분집합/상위집합여부를 판단할 수 있다...이건 좀 개념이 수학을 알아야 하네

print(set7==set8)   # 두 집합이 같은지를 비교 함

print(set7.isdisjoint(set8))    # 두 집합이 겹치는 부분이 있는지 확인

# 7. set 조작하기

set7.add(20)    # 왜 이건 ({})이 형태가 아니냐...
print(set7)
set7.remove(20) # 있으면 삭제, 없으면 에러 발생
print(set7)
set7.discard(3) # 있으면 삭제, 없으면 패스
print(set7)
set7.discard(99)
print(set7)

set7.pop()      # 세트에서 임의 값을 삭제 합니다. 없으면(비어있는 세트) 에러를 띄움
print(set7)

set8.clear()    # 모든 요소를 삭제

print(len(set9),set8)

# 8. set의 할당과 복사

#>> set은 일반적인 copy로 복사가 된다... 이거 무슨 기준이지?

set8 = set9.copy()
print(set8,"|",set9)
set9.add(88)
print(set8,"|",set9)

import copy

set10 = copy.deepcopy(set9)     
print(set9,"|",set10)

#>> deepcopy도 되네? 그럼 shallow copy를 써도 되는 시퀀스가 있고 deep copy를 해야 되는 것도 있가 이렇게 이해하면 되나?

# 9. 반복문으로 세트 표현

#>> for문을 통한 set 출력
for i in set9:
    print(i)

#>> set 표현식으로 set 초기화
set10.clear()
set10 = {i for i in {2,3,5,1,6,72}}
set11 = {i for i in range(1,20) if i % 2 == 0}
print(set10,"||",set11)
