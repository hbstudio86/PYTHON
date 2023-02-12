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

#>> zip으로 2-gram 만들기
#>> zip함수는 두 개 이상의 값을 하나의 튜플로 묶는 역할을 한다.

text = 'hello'
text2 = text[1:]    # 1~끝
print(len(text),len(text2))
two_gram = zip(text,text[1:])
two_gram2 = zip(text,text[1:])
#>> 위의 zip(text,text[1:])는
#   text[0],text[1]을 묶어서 튜플 형태로 two_gram[0]에 들어 간다. 즉 two_gram[0] = (text[0],text[1])이 된다.

print(tuple(two_gram))
print(list(two_gram2))
for i in two_gram:
    print(i[0],i[1],sep="")

#>> zip과 list 형식으로 N-gram 만들기

print(list(zip(['hello','ello','llo'])))
#>> 이 표현 방식의 경우 [~] 내의 hello ello llo가 하나의 리스트 덩어리이므로
#   문자열 덩이리 하나씩 튜플이 되어 zip에 묶이게 된다.
#   따라서 리스트 내의 문자열을 풀어써야 하는데 이를 리스트 언패킹이라 한다.
#   리스트 언패킹을 하려면 리스트 형태 앞에 *(애스터리스크)를 붙혀 주기만 하면 된다.

print(list(zip(*['hello','ello','llo'])))
#>> 이러면 리스트의 각 문자열이 3개의 별개 인자로 작용하게 된다.
#   즉, zip(hello를 담은 변수, ello를 담은 변수, llo를 담은 변수)와 같아 지게 되는것이다
#   llo가 가장 길이가 짧으니 튜플은 3개씩 3묶음이 만들어진다.


# 연습 문제 #

n = int(input())
text = input()
words = text.split()      
if (n > len(words)):
    print('wrong')
else:
    n_gram = [words[i:n+i:] for i in range(len(words)-n+1)]
    for i in n_gram:
        print(i)

# 심사 문제 #

with open('words.txt','r') as file:
    while True:
        _is_read = True
        _str_read = file.readline()
        _str_read = _str_read.strip('\n') #개행문자를 삭제
        if _str_read != '':
            lists = list(zip(_str_read,_str_read[::-1]))  #lists에 정방향 단어와 역방향 단어가 리스트 형식으로 저장 됨
            for i in lists:
                if i[0] != i[1]:
                    _is_read = False
                    break
            if _is_read == True:
                print(_str_read)
        else:
            break

