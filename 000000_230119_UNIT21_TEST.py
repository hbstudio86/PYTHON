## UNIT21 심사 문제 ##

import turtle as t

t.speed("slow")
t.shape("turtle")

n, line = map(int,input().split())
#i = 0

for i in range(n):
    #t.right((360/n)*2)
    #t.forward(line)
    #t.left(360/n)
    #t.forward(line)
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)
