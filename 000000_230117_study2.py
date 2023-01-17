## UNIT 19 별출력 ##

# 1. 계단식 별출력
#*
#**
#***
#****
#*****

i = 0
j = 0

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

print("==================================")
# 2. 사각형 별출력
#*****
#*****
#*****
#*****
#*****
for i in range(1,6):
    for j in range(5):
        print("*",end="")
    print()

print("==================================")
# 3. 대각선 별출력
#*
# *
#  *
#   *
#    *
for i in range(1,6):
    for j in range(i):
        if i == (j+1):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# 연습 문제 #

height = int(input())
x = 0
y = 0
z = 1
#for i in range(height-1,-1,-1):
for i in reversed(range(height)):
    for j in range(i):
        print(" ",end="")
    for j in range(z):
        print("*",end="")
    print()
    z+=2
