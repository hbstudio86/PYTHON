## UNIT 31 재귀호출 ##

# 1. 재귀 함수 구현하기

def Hello(n):
    if 0 == n:
        return
    n -= 1
    print("Hello World!")
    Hello(n)

Hello(10)

# 2. 재귀 호출로 팩토리얼 구하기 (책 안보고 스스로 코드 짜보기)

def f_fact(n):
    if 1 == n:
        return n
    return f_fact(n-1) * n

print(f_fact(4))

# 심사 문제 #

def fib(n):
    if 0 == n or 1 == n:
        return n
    return fib(n-1) + fib(n-2)

# 피보나치 수열은 앞 두 개의 피보나치 합을 출력하면 된다.
# 5의 피보나치 수는 5이다.
# 5의 앞의 수는 4(5-1)이고, 그 앞의 앞 수는 3(5-2)이다.
# 그럼 4의 피보나치는 역시 그 앞의 수와 그 앞의 앞수의 피보나치 수을 더하면 된다.
# 그럼 return은 fib(n-1)과 fib(n-2)의 합을 하면 되고
# 이것의 끝은 n이 0 혹은 1일때 0과 1을 리턴하는 것으로 마무리 하면 된다

for i in range(20):
    n = int(input())
    print(fib(n))

