## UNIT20 FizzBuss 문제 ##

# 규칙1. 1에서 100까지 출력
# 규칙2. 3의 배수는 Fizz 출력
# 규칙3. 5의 배수는 Buzz 출력
# 규칙4. 3과 5의 공배수는 BizzBuzz로 출력
i = 0

for i in range(1,101):
    if 0 == i % 3 and 0 == i % 5:   # 0 == i % 15
        print("FizzBuzz")
    elif 0 == i % 3:
        print("Fizz")
    elif 0 == i % 5:
        print("Buzz")
    else:
        print(i)

#>> 극단적으로 줄인 경우
#>> print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i) 의 형식으로 단축 시킬 수 있으나
#>> 후에 코드의 유지 보수를 위해서는 쉽게 풀어 써야 한다.

#>> 내가 지금 당장 작성하기 쉽지만 남들이 보기 힘든 형식 vs
#>> 내가 지금 힘들게 작성하지만 남들이 보기 쉬운 형식, 두 형태로 만들 수 있다

# 심사 문제 #

start,end = map(int,input().split())  # 정수 두 개 받기
i = 0

for i in range(start,end+1):
    if 0 == i % 5 and 0 == i % 7:   
        print("FizzBuzz")
    elif 0 == i % 5:
        print("Fizz")
    elif 0 == i % 7:
        print("Buzz")
    else:
        print(i)
print("end")
