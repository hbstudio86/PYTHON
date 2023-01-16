## UNIT16 for 문 ##

# 1. 문법

for i in range(100):
    print("[",i,"] hello World!")

#for i in 100:
#    print("[",i,"] hello World!")
#>> range(~) 형태를 무조건 사용해야 한다.

# 2. range 응용

for i in range(3,8):    #시작과 끝
    print(i,'번째 안녕!')


for i in range(0,11,2): #시작과 끝, 증감
    print(i,"hello~")
#>> for (int i = 0 ; i < 11 ; i+2)

for i in range(10,-1,-1):
    print("Count down!:",i)

for i in reversed(range(10)):
    print("Reversed~:",i)

for i in range(10):
    print(i)
    i = 99
#>> 기존 C에서는 loop가 시작될 때 i의 값을 판단하는데
#   파이썬에서는 값이 덮어쓰기 때문에 이런 형태에서도 정상적으로 값이 출력된다.

# 3. 입력한 수로 반복하기

count = int(input("숫자를 입력하세요:"))

for i in range(count):
    print(i,"번째")

# 4. 시퀀스 객체로 반복문 진행하기

a = [10,20,30,40,50]

for i in a:
    print(i)

for a in a:
    print(a)

for text in 'Hello World!':
    print(text,end="")

print("\n")

for text in reversed("Hello World!"):
    print(text,end="")
print()

# 연습 문제 #

num = int(input("구구단 단수를 입력하세요:"))

for i in range(1,10):
    print(num,"*",i,"=",num*i,sep=" ")

