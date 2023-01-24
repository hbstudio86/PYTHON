## UNIT23 2차원 리스트 ##

# 1. 문법

l1 = [[1,2],[3,4]]
print(l1)

#>> 기존의 2차원 배열과 같은 형식

# 튜플과 리스트

t1 = ((1,2),(3,4))  #튜플에 튜플
t2 = ([1,2],[3,4])  #튜플에 리스트
l2 = [(1,2),(3,4)]  #리스트에 튜플

#>> t1의 경우 개별 원소 변경 불가, 행의 변경 불가
#   t2의 경우 개별 원소 변경 가능, 행의 변경 불가
#   l2의 경우 개별 원소 변경 불가, 행의 변경 가능

print(t1,t2,l2,sep='\n')

t2[0][0] = 100
l2[0] = (100,100)

print(t1,t2,l2,sep='\n')

l3 = [[1,2],[1,2],[1,2],[1,2]]

print(l3)

from pprint import pprint
pprint(l3,indent=4,width=20)

# 2. 반복문으로 제어하기

for x,y in l3:
    print(x,y)

for i in l3:
    for j in i:
        print(j,end=' ')
    print()
