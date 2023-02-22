## UNIT 32 람다 표현식 ##

# 1. 람다 표현식 : 간단하게 익명 함수를 만든다

def plus_ten(x):
    return x+10

plus_ten2 = lambda x: x+10

#>> 두 표현은 같다
#   하지만 람다표현식은 바로 사용하지 못한다.
#   람다 표현을 담은 함수가 없기 때문이다.
#   따라서 람다 표현식을 변수에 넣어줘야 한다.

print(plus_ten(1))
print(plus_ten2(1))
print((lambda x : x+10)(1))

#>> 람다 표현식 내부에서 변수를 선언하고 초기화 할수 없다
#   즉, lambda x : y = 10, x + y 와 같이 y를 선언한 다음 초기화 할 수가 없다

#x,y,z = map(int,input().split())
#print(x,y,z)

x,y,z = map(plus_ten,[1,2,3])
print(x,y,z)

k = list(map(plus_ten,[1,2,3]))
print(k)

t = list(map((lambda x : x + 10),[1,2,3]))
print(t)
# 람다 표현식을 쓰면, 일회용을 사용할 함수를 만들지 않아도 그와 동일한 효과를 얻을 수 있다.

# 2. lambda 표현식에서 조건부 사용하기

# lambda 매개변수들:식1 if 조건식 else 식2 -> 식1은 조건식이 참일때 반환값, 식 2는 거짓을 때 반환값을 말한다. 더럽게 햇갈리네
#   map을 사용하여 리스트 a에서 3의 배수를 문자열로 변환
a = [1,2,3,4,5,6,7,8,9,10]
b = list(map((lambda x : str(x) if x % 3 == 0 else x),a))   #-> 람다를 둘러싼 괄호는 삭제해도 된다.
print(b)

# if를 사용했다면 else를 무조건 사용해야 한다. if만 사용하면 문법syntax 오류가 발생한다.

c = list(map(lambda x : str(x) if x % 3 == 0 else float(x) if x % 2 == 0 else x,a))
#            람다   인수: 참일 때 / 조건식1   / 거짓일때 , 거짓일때 조건식2 / 거짓을 때 , 인자
print(c)

# 람다 표현식으로 조건식을 사용하면 복잡하고 가독성만 떨어진다. 차라리 이런 경우에는 함수를 만들자...

#>> 복수의 객체를 사용하기

d = [11,12,13,14,15,16,17,18,19,20]

e = list(map(lambda x,y:x*y,a,b))

print(e)


# 3. filter 사용하기

#>> 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져 오기 (true)

def f(x):
    return x > 5 and x < 10
# x가 5보다 크고 10보다 작은 조건일 때 True를 반환한다.

g = list(filter(f,a))
print(g)

h = list(filter(lambda x : x > 5 and x < 10,a))
print(h)

# 4. reduce 사용하기 : 두개의 결과 값을 더해서 출력하는 함수....라는데 무슨 용도인지 감이 안온다..

from functools import reduce
def f2(x,y):
    return x+y

def f3(x,y,z):
    return x+y+z


print(reduce(f2,a))
#print(reduce(f3,a))

print(reduce(lambda x,y:x+y,a))


# 연습문제 #

files2 = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1,files2)))

test111 = '105.jpg'

print(test111.find('.jpg'))

#실행 결과
#['1.png', '10.jpg', '2.jpg', '3.png']

# 심사 문제 #

# 점.을 찾아서 zfill로 0을 채워주면 되겠네
files = ['97.xlsx', '98.docx', '99.docx', '100.xlsx', '101.docx', '102.docx']


print(list(map(lambda x: x.zfill(len(x)+2) if x.find('.') == 1 else x.zfill(len(x)+1) if x.find('.') == 2 else x,files)))
