## UNIT 28 회문 판별과 N-gram 만들기 ##

# 1. 회문 판별

#>> 앞뒤가 같은 문자열을 회문이라고 한다.
#   level SOS rotator 등..

#>> for 문으로 회문 검사 하기 (자작)

print("문자열을 입력하세요")
#str1 = "level"
str1 = input()
sHalf = int(len(str1)/2)
for i in range(0,sHalf):
    if str1[i] != str1[-1-i]:   # 두 문자를 비교
        print("회문이 아닙니다.")
        break
    if i == sHalf -1 :
        print(f'{str1} 은/는 회문입니다.')

#>> for 문으로 회문 검사 하기 (서적)

word = input("단어를 입력하세요: ")
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        is_palindrome = False
        break
print(is_palindrome)

#>> 시퀀스 반전으로 검사 하기 (자작)

import copy

str2 = input("input string: ")
str2R = copy.deepcopy(str2) # 문자열을 복사 함.

for index,i in enumerate(reversed(str2R)):
    if index > len(str2R) / 2:
        print("회문 입니다.")
        break
    if str2[index] != i:
        print("회문이 아닙니다.")
        break


#>> 시퀀스 반전으로 검사 하기 (서적)

str3 = input("input strings: ")

print(str3 == str3[::-1])   # 함수의 리턴처럼 r-value 형태를 취하면 그 결과를 변환시켜 주는 것인가??
print(list(str3) == list(reversed(str3)))

#>> 겁나 간단하네. 뭐랄까? C 처럼 하나하나 짤 필요 없이 그냥 된다고 생각하는 형태면 다된다는 느낌?


#>> join 과 reversed

word = 'level'
print(word == ''.join(reversed(word)))

#>> 이게 왜 되는것인지 모르겠네??


# 2. N-gram 만들기

#>> N개의 문자를 연속으로 추출하는것을 말함
#   N이 2이면 he el ll lo 같이 중첩되게 2글자씩 추출한다.

for i in range(len(word)-1):
    print(word[i],word[i+1],sep='')
