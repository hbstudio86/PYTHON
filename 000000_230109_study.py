## UNIT9 문자열 사용하기 ##
Hello = 'Hello Wolrd'
print(Hello)
Hello2 = "Hello\nWorld!\n!!"
print(Hello2)
h3 = "TEST 'is Test"    #"과 '의 혼용은 문자열에서 해당 문자를 사용하기 위함
h4 = 'Test "Just"TEST'  
print(h3,h4)
h5 = """hhh'kkk'tkdk"""
print(h5)

## UNIT10 리스트와 튜프 사용하기 ##
#리스트 생성 및 초기화
ar1 = [10,11,12,13,14,15]   #배열처럼 생성하였다
print(ar1)
#indexing이 가능한가?
print(ar1[0])   #index로 접근이 가능하다
#또한 편하게 여러 자료형을 묶어서 쓸수가 있다
ar2 = ['hello',333,1.567,True]
print(ar2)
#각 원소들의 자료는??
print(type(ar2[0]))
print(type(ar2[1]))
print(type(ar2[2]))
print(type(ar2[3]))

#리스트 멤버를 지정하지 않게 초기화 할 수도 있다.
ar3 = []     #문법 1
ar4 = list() #문법 2

#연속된 값으로 초기화
ar5 = list(range(10))   #이러면 0~9까지 생성된다(컴퓨터는 0부터 시작)
print(ar5)
ar6 = list(range(3,10)) #이렇게 특정 숫자의 범위를 지정할 수 있다 (3~9)
print(ar6)
ar7 = list(range(0,10,2))   #시작, 끝, 증가폭을 지정할 수 있다.
print(ar7)

#튜플이라는 형태도 가능하다
tp1 = (10,20,30)    #리스트와 비슷하나 자료의 변경이 되지 않는다고 함
print(tp1)
tp2 = 11,22,33      #()없이 사용이 가능하다
print(tp2)

tp3 = ("Tuple",22,12.4,False)   #튜플 또한 여러 자료형을 담을 수 있다
print(tp3)

#튜플은 자료를 보호해야 하는 마치 Const와 같다고 생각한다.
#원본을 보존해야 할 경우

#만약 1개 짜리 튜플을 사용해야 한다면?
#tp4 = (33) 이러면 튜플이 되는가?
print(type(tp3))    #어떤 값이 나오는가? => class tuble로 나온다
tp4 = (33)
print(type(tp4))    #튜플로 인식하지 않고 정수형으로 나온다
#하나짜리 튜플을 사용하려면...(값,)의 문법을 이용해야 한다.
tp5 = (88,)
print(type(tp5))    #하나짜리 튜플

#튜플--->리스트 / 리스트--->튜플로 형변환이 가능하다
print("튜플--->리스트")
print("Type tp1:",type(tp1))
list(tp1)   #형변환
print("Type tp1:",type(tp1))
print(tp1)
print("리스트--->튜플")
print("Type ar1:",type(ar1))
tuple(ar1)   #형변환
print("Type ar1:",type(ar1))
print(ar1)
#이러면 리스트의 내용을 보호 할 수가 있다 const arr처럼 말이다
#안되는데??
#아... 형변환이 아니고 임시로 그 자료형을 변경해주는 것이었다.
print(list(tp1))        #튜플을 리스트"처럼"사용할 수 있게 해준다
print(type(list(tp1)))  #튜플이 리스트형이 되었다

