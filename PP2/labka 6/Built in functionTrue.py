import math
import time
#EX1
x = int(input())
list1 = list()
for i in range(x):
    y = int(input())
    list1.append(y)
    x-=1
t = iter(list1)
answer = 1
for i in range(x):
    answer = next(t)
print(answer)
#EX2
srt = str(input())
upper = 0
lower = 0
x = len(srt)
for i in srt:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower+=1
print(lower)
print(upper)
#EX3
str1 = str(input())
x = iter(str1)
answe = True
for i in str1[::-1]:
    if i!=next(x):
        answe = False
        break
print(answe)  
#EX4
n = int(input())
delay_ms = int(input()) 
result = math.sqrt(n)
time.sleep(delay_ms / 1000)
print(result)
#EX5
n=int(input())
mylist=list()
for i in range(n):
    x=input()
    if x=="true" or x=="True":
        mylist.append(True)
    else:
        mylist.append(False)
mytuple=tuple(mylist)
t=all(mytuple)
print(t)
