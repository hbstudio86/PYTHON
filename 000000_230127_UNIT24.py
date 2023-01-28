## UNIT24 문자열 응용 ##

# 1. 문자열 바꾸기
#>> replace(기존 문자열,새 문자열)

"HELLO EARTH".replace("EARTH","MARS")
str1 = "Hello World!"
print("바꾸기 전 :",str1,end="")
str1 = str1.replace("World","Python")
print("바꾼 후 :",str1)

#>> replace() 메서드는 문자열을 직접 바꾸지 않는다.
#   바꾼 문자열의 결과를 반환 한다.
#   따라서 바꾼 문자열로 적요하기 위해서는 해당 함수에 재할당 해야 한다.

# 2. 문자 바꾸기
#>> translate()

str3 = 'apple'
str2 = str.maketrans('aeiou','12345')
print(str2)     # dictionary의 형태로 저장이 되네?!
str3 = str3.translate(str2) # dictionary형태의 str2를 str3와 대조하여 맞는 것을 치환 하는 형태일 것으로 보이네
print(str3)

dic1 = {'a':1,'b':2}
print(dic1)

print(dic1['a'])

# 3. 문자열 분리하기
#>> split() 메서드는 스페이스를 기준으로 문자열을 분리한다.

str4 = "Hello Wolrd, My name is jk!! !"
strlist = str4.split()
print(strlist)


# 4. 문자열 합치기
#>> join()

str5 = '/'.join(strlist)
print(str5)

# 5. 대/소문자 변경하기
#>> 기존 C/C++과 비슷한 메서드를 이용한다.

str6 = "HeLlo WoRlD"
print("원래 문자:",str6,end='')
print(" 대문자 변환:",str6.upper(),end='')
print(" 소문자 변환:",str6.lower())

# 6. 공백문자 삭제 하기
#>> lstrip, rstrip, strip 메서드를 이용하는데 VB의 trim과 유사하네

str7 = "   HOHOHO   "
print("원래   문자:",str7)
print("좌공백 삭제:",str7.lstrip())
print("우공백 삭제:",str7.rstrip())
print("양공백 삭제:",str7.strip())


# 7. 특정 문자 삭제 하기
#>> 사용 빈도가... 높은가?

str8 = ",.# 1234 ,.#"
print("원래   문자:",str8)
print("좌공백 삭제:",str8.lstrip(",."))
print("우공백 삭제:",str8.rstrip("#"))
print("양공백 삭제:",str8.strip(","))

#>> 제일 외곽의 특정 문자들이 삭제가 된다?

# 8. 문자열 정렬
#>> C/C++계열에서 필드 설정과 비슷해 보인다.

str9 = 'TEST'
print(str9.ljust(10))
print(str9.rjust(10))
print(str9.center(10))  # 이건 또 왜 Center여...

# 9. 메서드 체이닝
#>> 메서드를 연결해 사용할 수 있다.

str10 = 'AbCdEfGHIjkl'
print('원래 str10의 값:',str10)
print('str10.center(20).upper() :',str10.center(20).upper())

# 10. 0으로 채우기
#>> 빈 필드에 0으로 채워 넣는다. C/C++ 계열에서 %02d와 같은 필드 옵션과 비슷해 보인다.

print(str9.zfill(10))

# 11. find 문자열 찾기
#>> 문자열을 찾는다.

print(str10.find('GH'))
print(str10.find('gh'))
print(str10.index('GH'))
print(str10.rfind('GH'))

print(str9.count('T'))

# 12. formatting 이용하기
#>> C/C++ 계열에서의 포매팅과 유사하다

str11 = 'Hello'
num1 = 10
flo1 = 34.86

print(" %s ~ 나는 올해 %03d살이고, 몸무게는 %06.2f 야~~" % (str11 , num1 , flo1)) # 번잡하네...

#>> 좀 더 파이썬 스럽게 형식을 사용하자면...

print(str10,'{0} {1} {2}'.format(str11,num1,flo1))

print(f'Hello {str11} {num1} {flo1}')
