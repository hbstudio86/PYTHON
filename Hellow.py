print("Hello, world!")
print('hello, world!')
#230103
#comment using
print("세미콘론사용"); #this!
print("붙혀서 쓰기"); print("이건 되나??")
#indentation
#int x = 10
if (5+5) == 10:
    print('10')
#code block
if (5+5) == 10:
    print(10)
    print('this')
#operator
print(3+3) #+op
print(2-1) #-op
print(2*4) #*op
print(5/2) #/op
print(5//2) #//op
print(5**2) #**op
print(5%2) #%op
#int()
print(int(3.3));
print(int(5/2));
print(int('100'));
#type()
print(type(10)); print(type(11.1));
type(10);   #no output
#divmod()
print(divmod(5,2));
#bin oct hex ---> dec
print(0b1101);print(0o37);print(0x1f);
#int ---> float
print(float(3));print(float('5'));
x = 10
print(type(x));
##230104
#복수의 배열 초기화
x1, x2, x3 = 11,12,13
print(x3);print(x2);print(x1);
#python에서는 null이 None이다 (대소문자 구분함)
del x1
x1 = None
print(x1)
#python에서는 Rvalue를 간편하게 출력할 수 있다
print(x2 + 10); print(x2);
#음수 양수 표현도 가능
print(-x2);print(+x2);
#input() 입력 함수
xx = input()
print(xx)
print(type(xx))
print('값을 입력하세요');xx = input();print(xx); #이런방식이 있고
xx = input('값을 입력하세요: ');print(xx); #이런 방식도 있다
#막간을 이용한 문제 풀이
aa = input('숫자를 입력하세요: ')
bb = input('숫자를 입력하세요: ')
#print(aa+bb);   #이러면 문자열 연결형태로 출력
#int로 형변환 시켜 준다면?
print(int(aa)+int(bb));
#split()
aa,bb = input('두개의 숫자를 입력하세요: ').split() #화이트 스페이스로 구분
#C의 Scanf("%d %d",...)와 같은 기능을 한다
print(int(aa)+int(bb))
#map 함수
aa, bb = map(int,input('숫자 두개를 입력하세요: ').split());  #신기하구만...
print(aa+bb);
aa, bb = map(int,input('숫자 두개를 입력하세요: ').split(',')) #split에 구분자를 입력하면 구분됨
print(aa+bb)
#정수 -10 20 30을 받고 합산을 출력하라
aa, bb, cc = map(int,input('정수 3개를 입력하라: ').split())
print(aa+bb+cc)



