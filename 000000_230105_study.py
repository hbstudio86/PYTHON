#a,b,c,d = map(int,input().split())
#e = a+b+c+d
#e //= 4
#print(e)
## UNIT 7 ## : 출력 방법
#print() 여러번 출력 하기
print(1,2,3);print('Hello','WORLD!');
#print(var1,var2, sep = '') 이런식으로 각 변수 출력에 형식을 지정할 수 있다.
#마치 C의 Printf에서 형식 지정자와 비슷하다
print(1,2,3, sep = '_') #1_2_3
print(1,2,3,sep="/")    #1/2/3
print(1,2,3,sep="x")    #1x2x3
#기존의 C언어와 마차가지로 이스케이프 문자 삽입이 가능하다
print(1,2,3,sep='\n')   #ENTER Key
print("1\n2\n3\n")      #String Type
print(1,2,3,sep='\t')   #TAB Key
print(1,2,3,sep='\r')   #Reverse...?? CAN?
#print(값, end='')의 형태를 쓰면 print여러개를 한줄로 쓸수 있다
#굳이....
print(1,end='')
print(2,end='')
print(3)        #putchar와 비슷한듯하다
#두 개 이상의 print함수에 대해 하나로 연결 해줄 때 사용하네...
import sys
print(sys.getrefcount(1))   #충격적이게도 python에서는 상수라고 했던 것도
                            #모두 객체로 취급한다.
                            #그래서 해당 객체가 몇 번 사용했는지 알 수 있다
## UNIT 8 ## : 비교 논리 연산
print("복사본 TEST")
