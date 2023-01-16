## UNIT 17 While 문 ##

# 1. 문법

x = 10

while x < 20:
    print(x)
    x += 1

print(x)

while x > 0:
    print(x)
    x -= 1

# 2. range 정하지 않기

import random   #난수 생성기...근데 구분이 안되네.

print(random.random())
print(random.random())
print(random.random())
print(random.randint(1,6))  #범위 난수

i = 0
while i != 4:
    i = random.randint(1,6)
    print(i)
a = [1,2,3,4,5,6]
print("============NEW==========")
i = 0
while i != 4:
    i = random.choice(a)
    print(i)

i = 0
print("============NEW==========")
while True: #무한 루프
    i += 1
    print(i)
    if 10 == i:
        break
