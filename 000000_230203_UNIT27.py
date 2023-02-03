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
