## UNIT13 IF문 ##

############################################

# if 조건 :
#    내용...  들여쓰기를 무조건 해줘야 한다



############################################


# 1. if문 사용

x = 10
if 10 == x:
    print("x의 값은...",x)
#>> x = 10으로 오타 칠 수 있으니
#>> 가급적으로 10 == x 처럼 상수를 앞으로

# 2. if문 생략
# if문을 그냥 통과 할 수 있다.

if 100 == x:
    pass    #TODO
#>> 이런식으로 if문의 형태를 유지하면서 통과 할 수 있다. 주석처리는 꼭 할 것

# 3. 여러 if문 사용
# 칸 띄우기만 잘 지키면 된다.

if 5 < x:
    print("x는 5이상")
    if 20 > x:
        print("x는 20이하")
    if 10 == x:
        print("x는 10입니다.")
if 33 != x:
    print("x는 33이 아닙니다.")


# 연습문제

price_1 = int(input())
couphon = input()

if "Cash3000" == couphon:
    price_1 -= 3000
    print(price_1)
if "Cash5000" == couphon:
    price_1 -= 5000
    print(price_1)

