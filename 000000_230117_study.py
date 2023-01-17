## UNIT18 Break continue ##

#>> 기존 C언어에서 사용한 것과 같다

# 1. 문법 (break)

x = 0

while True:
    print (x)
    x += 1
    if x == 100:
        break

for x in range(100):
    print(x)
    if 40 == x:
        break

# 2. 문법 (continue)

x = 0

for x in range(100):
    if 0 == x % 2:
        continue
    print(x)

x = 0

while 100 > x:
    x += 1
    if 0 == x % 2:
        continue
    print(x)


# 연습 문제 #

start, stop = map(int,input().split())
i = start
while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break    
    print(i,end=" ")
    i += 1
