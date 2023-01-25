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

for i in range(len(l3)):
    #for j in range(len(i)):
    for j in range(len(l3[i])):
        print(l3[i][j],end=' ')
    print()

i = 0
while i < len(l3):
    x,y = l3[i];
    print(x,y);
    i+=1;

i = 0
j = 0
while i < len(l3):
    while j < len(l3[i]):
        print(l3[i][j],end=' ')
        j+=1
    print()
    i+=1
    j=0

# 3. for문으로 2차원 리스트 만들기

l4 = [] # 빈 리스트를 하나 만들고
x = 0
y = 0
for x in range(10):
    inl4 = []   # 내부 원소를 저장할 빈 리스트 생성 계속 초기화 된다.
    for y in range(2):
        inl4.append(0)
    l4.append(inl4)

print(l4)

# 4. 리스트 표현식으로 2차원 리스트 만들기

l5 = [[ j for j in range(2)] for i in range(3)]
print(l5)

# 5. 2차원 리스트의 할당과 복사

#>> 2차원 리스트는 copy 메서를 이용해도 shalow copyㅏ밖에 되지 않는다.

test1 = [[1,2],[3,4]]
test2 = test1           #앝은 복사
print(test1,test2,sep="\n")
test1[0][0] = 200
print(test1,test2,sep="\n")
test3 = test1.copy()
print(test1,test3,sep="\n")
test1[0][1] = 999
print(test1,test3,sep="\n")

import copy

test4 = copy.deepcopy(test1)
print(test1,test4,sep="\n")
test1[1][0] = 444
print(test1,test4,sep="\n")

