## UNIT15 elif ##

#>> C언어에서의 else if와 같은 역할을 한다.

# 1. elif

x = 30
if 10 == x:
    print("x는 10입니다.")
elif 20 == x:
    print("x는 20입니다.")
else:
    print("x는 30입니다.")


# 연습문제

age = int(input())
balance = 9000  #카드 잔액

if 12 >= age:   #12세 이하면..
    balance -= 650
elif 13 <= age and 18 >= age:
    balance -= 1050
else:
    balance -= 1250

print(balance)
