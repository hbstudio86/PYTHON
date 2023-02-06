## UNIT 27 파일 사용하기 ##

# 1. 파일에 문자열 쓰기, 읽기

file = open('hello.txt','w')
file.write('hello world')
file.close()

#>> c/c++의 file과 유사하게 작동한다.
#   c/c++의 경우
#   FILE* fp; 로 file 포인터를 선언하고
#   fp = fopen('hello.txt','w');    로 file을 어떤 모드로 열지 확인
#   // 물론 여기에 if (fp == null){...} 로 파일 open에 실패 했을 때를 제
#   fputs("Hello world",fp);        로 스트림을 통해 내용 출력
#   fclose(fp)                      로 스트림을 닫아 준다.

file = open('hello.txt','r')
s = file.read()
print(s)
file.close()

#>> 파일 객체를 자동으로 당아주는 문법

with open('hello.txt','r') as file:
    s = file.read()
    print(s)


# 2. 여러줄 파일 쓰고 읽기

with open('hello.txt','w') as file:
    for i in range(10):
        #file.write('hello world {0}\n'.format(i))
        file.write(f'hello worlds {i}\n')

#>> 쓰기 모드 w라서 그냥 써지기만 한다. 갱신 모드 a를 써야 추가가 되는듯 하네

# 3. 리스트 문자열 출력

list1 = ['안녕하세요\n','파이썬 \n','코딩 도장입니다.\n']

with open('hello.txt','a') as file:
    file.writelines(list1)

#>> 역시 추가 모드는 C/C++계열과 별바 다를게 없구만

with open('hello.txt','r') as file:
    list2 = file.readlines()

print(list2)

#>> readlines()는 일괄로 모든 문자열을 읽어오는 기능으로 보인다?

with open('hello.txt','r') as file:
    list3 = None    # while문 때문에 none으로 초기화 하였다.
    while list3 != '':
        list3 = file.readline()
        print(list3.strip('\n'))


with open('hello.txt','r') as file:
    for i in file:
        print(i.strip('\n'))

#>> for문을 통해 좀 더 간단하게 표현할 수 있다.
#   책에서는 file 객체가 이터레이터, 즉 포인터의 객체화된 것이라고 소개하고 있다.

# 4. 파이선 객체 저장하기

#>> 객체 ----> 파일 : 피클링
#   파일 ----> 객체 : 언피클링

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
score = {'국어':90,'영어':95,'수학':85,'과학':82}

with open('james.p','wb') as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(score,file)


#>> 진짜... 메서드 제시를 전혀 안한다...ide 때문에 그런가...

with open('james.p','rb') as file:
    name2 = pickle.load(file)
    age2 = pickle.load(file)
    address2 = pickle.load(file)
    scores2 = pickle.load(file)

print(name2,age2,address2,scores2,sep='\n')

# 심사 문제 #

with open('words.txt','r') as file:
    ss = file.read()
print(ss)

lists = ss.split()

print(lists)

for i in lists:
    if "c" in i:
        print(i.strip(',.'))
