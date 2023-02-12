## UNIT30 함수에서 위치 인수와 키워드 인수 사용하기 ##

# 1. 위치 인수
#>> 함수에 인수를 순서대로 넣고 출력하는 것을 위치 인수라 한다.

def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

print_numbers(1,2,3)
    
#>> 만약 list를 print_numbers에 인수로 넣어야 한다면 어떤 방식으로 넣어야 하는가?
#   print_numbers(list[],list[],list[])의 형태로 넣어야 하겠지?
