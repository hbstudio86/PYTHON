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
    if 0 == n:
        return 0
    return fib(n-1) + n

n = int(input())
print(fib(n))
