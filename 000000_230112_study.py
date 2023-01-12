## UNIT14 else ##

# 1. else 사용
# 기존의 언어들과 같은 기능을 하고 있다.

x = 300

if 200 == x:
    print("x는 200입니다.")
else:
    print("x는 200이 아닙니다.")
#이것을 람다 형식으로 사용할 수 있다    
y = x if 60 == x else 0     #아.. 이건 마치 3항자랑 비슷해 보이네 60 == x ? y = x : y = 0 ;
print(y)

# 2. 참이란?
# 기존 언어와 마찬가지로 0이면 거짓, 0이 아닌 것은 모두

if None:
    print("참")
else:
    print("거짓")
if 0:
    print("참")
else:
    print("거짓")
if False:
    print("참")
else:
    print("거짓")
if True:
    print("참")
else:
    print("거짓")
if 1:
    print("참")
else:
    print("거짓")
if 10:
    print("참")
else:
    print("거짓")
if 5.6:
    print("참")
else:
    print("거짓")

# 3. 여러 조건 비교

if 200 < x and 600 > x:
    print("x는 200보다 크고 600보다 작습니다.")
#>>위의 조건식을 더욱 간단하게 할 수 있다.
if 200 < x < 600:
    print("x는 200과 600사이 이다.")

# 연습
a, b, c, d = map(int,input().split())
sum = a + b + c + d
sum /= 4
if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100 and 0 <= d <= 100:
    if 80 <= sum:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
    
