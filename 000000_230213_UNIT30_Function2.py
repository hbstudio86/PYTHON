## UNIT30 함수에서 위치 인수와 키워드 인수 사용하기 ##

# 1. 위치 인수
#>> 함수에 인수를 순서대로 넣고 출력하는 것을 위치 인수라 한다.

def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

print_numbers(1,2,3)
    
#>> 만약 list를 print_numbers에 인수로 넣어야 한다면 어떤 방식으로 넣어야 하는가?
#   print_numbers(list[],list[],list[])의 형태로 넣어야 하겠지?

list1 = [1,2,3] # 이것을 함수에 넣으려면...

print_numbers(list1[0],list1[1],list1[2]) # 이런식으로

# 하지만 간단하게 리스트 자체를 넘겨줘도 된다.
# 다만, 리스트 객체 앞에 *를 붙혀서 사용하면, 위와 같은 효과를 가질 수 있다.

print_numbers(*list1)

# 그럼, 리스트의 멤버수와 함수의 매개변수의 수가 다르다면?

list2 = [1,2,3,4]

# print_numbers(*list2) # 당연히 안된다.

# 만약 입력되는 매개 변수의 갯수가 정해져 있지 않다면??

def print_d_numbers(*args):
    for i in args:
        print(i)

print_d_numbers(*list1)
print_d_numbers(*list2)

# 고정 인수와 가변 인수를 같이 사용하고자 한다면...

def print_c_numbers(a,*args):   # 이런식으로 고정,가변 인수를 지정해주면 된다. 단 순서는 항상 가변인수가 뒤이다.
    print(a)
    print(args)

print_c_numbers(1,*list2)

# 2. 키워드 인수 (default 매개변수?)

def person_info(name = '홍길동',age = 30,address = '서울시 영등포구 여의도동'):
    print(name)
    print(age)
    print(address)


person_info('이재욱',30)
person_info(30,'KOREA') # 이것도 default 매개변수의 규칙과 같은 것으로 보인다.


# 3. 키워드 인수, dictionary unpcking 사용

dict1 = {'name':'James','age':50,'address':'USA'}

person_info(**dict1)

# dictionary를 언패킹할 때에는 **두개를 사용한다.
# 그리고 dictionary의 키와 매개변수의 명칭이 같아야 한다. (물론 갯수도 같아야 한다.)
# 언패킹시 *를 하나만 사용하면 키만 언패킹이 된다.

person_info(*dict1)

# 이 역시 가변인수로 취급할 수 있다.

def person_infos(**args):
    for key, value in args.items():
        print(key,value)

person_infos(**dict1)

x,y,z,k = 1,2,3,4

def test_f(*args):
    print(type(args))
    return max(args)
    

print('max :',test_f(x,y,z,k))

print('max2:',test_f(*[x,y,z,k]))

print('max3:',test_f(*list2))



# 심사 문제 #

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    return min(args), max(args)

def get_average2(korean=None, english=None,mathematics=None, science=None):
    count, total = 0, 0
    if korean != None:
        count += 1
        total += korean
    if english != None:
        count += 1
        total += english
    if mathematics != None:
        count += 1
        total += mathematics
    if science != None:
        count += 1
        total += science
    if 0 == count or 0 == total:
        return 0
    else:
        return total / count


def get_average(**args):
    print(type(args))
    return sum(args.values()) / len(args.keys())



min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
