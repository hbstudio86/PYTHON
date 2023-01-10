## UNIT11 시퀀스 자료형 활용하기 ##
#파이썬에서는 리스트, 튜플, 문자열, range와 같이 연속적으로
#data가 저장되어 있는 것을 시퀀스 자료형이라 한다.
#시퀀스 자료형은 모두 동일한 연산자를 공유 한다

#1. 멤버에 해당값이 있는지 확인
ar1 = list(range(0,11))
print("ar1 in 3? = ",3 in ar1)
print("ar1 in 100? = ", 100 not in ar1)

#2. +연산자를 통해 시퀀스 자료형끼리 묶을 수 있다 (합친다.)
ar2 = list(range(11,20))
ar3 = []
print("ar1 = ",ar1,"\nar2 = ",ar2,"\nar3 = ",ar3)
ar3 = ar1 +ar2
print("ar1 = ",ar1,"\nar2 = ",ar2,"\nar3 = ",ar3)

#3. 시퀀스 객체 반복하여 만들기
ar4 = [99,98,97] * 3
print(ar4)

#4. 시퀀스 객체 멤버수 구하기
print("ar1 member:",len(ar1))
print("ar2 member:",len(ar2))
print("ar3 member:",len(ar3))
print("ar4 member:",len(ar4))
#range가 생성하는 숫자의 개수를 구할 수 있다
print(len(range(0,10,2)))   #자주 사용함
print(len("Hello"))

#5. 원소에 접근 (list, tuple, range로 생성된 객체 등...)
print(ar1[3])
print(ar1.__getitem__(3)) #이렇게도 쓸 수 있다

#6. 음수 인덱스
#특이하게 인데스 값을 음수로 지정할 수 있다.
print(ar1[3],ar1[-8],sep="//")
# ar1 [0] [1] [2] [3]
# ar1 [-4] [-3] [-2] [-1]

#7. 원소에 값 할당 : ONLY TYPE LIst
print(ar1)
ar1[5] = 100
print(ar1)

#8. 원소 삭제 하기 : ONLY TYPE List
del(ar1[5]) #del ar1[5] 형태도 가능하다.
print(ar1)

#9. 시퀀스 자르기(슬라이스)
at5 =[]
ar5 = ar1[0:4]  #0~3까지의 원소들이 ar5로 전달된다. ar1은 멀쩡하다
print(ar5)
#인덱스 위치도 건너 뛸 수 있다.
ar6 = []
ar6 = ar3[0:11:2]
print(ar6)
#인덱스 지정범위를 생략할 수도 있다 (모든 번호를 생략하면 멤버 전체를 불러온다.)
ar7 = []
ar8 = []
ar7 = ar3[:8]   #시작부터 7번 index까지
ar8 = ar3[8:]   #8번 index부터 끝까지
print(ar7,ar8,sep="\n")
#[:7:2]의 형태나, [7::2]의 형태나 모두 사용이 가능하다 (for문이랑 비슷하네)
#튜플 또한 인덱스 접근은 []로 하니 혼동하지 말것
s1 = slice(4,7)
print(ar3[s1],type(s1),s1,sep="//")
print(ar4[slice(2,None,2)])  # 시작, 끝, 증감?
#슬라이스를 통한 멤버 지정 할당
ar4[2:6] = 'k','k','k','k'
print(ar4)
ar4[0:7:2] = 'a' , 'a' , 'a', 'a'   #영역과 값의 갯수가 정확히 일치 해야 함
print(ar4)
#del로 슬라이스 삭제
del ar4[2:4]
print(ar4)
print(ar1)
del ar1[-5::1]
print(ar1)
