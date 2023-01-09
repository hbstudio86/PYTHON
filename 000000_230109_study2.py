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
