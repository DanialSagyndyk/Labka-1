import math
import time

#EX1
def all(n):
    cnt = 1
    for i in n:
        cnt *= i
    return cnt

x = int(input())
my_list = list()
while x>0:
    y = int(input())
    my_list.append(y)
    x-=1
result = all(my_list)
print(result)

#EX2
def sum_of_world(s):
    upper = 0
    lower = 0
    x = len(s)
    for i in s:
        if i.isupper():
            upper +=1
        elif i.islower():
            lower+=1
            
    return upper, lower
srt = str(input())
result = sum_of_world(srt)
print(result)

#EX3
def polind(s):
    return s==s[::-1]
    
str1 = str(input())
if polind(str1):
    print("polindrom")
    
else:
    print("No")

#EX4
def call_sqrt(n):
    result = math.sqrt(n)
    print("Square root of n is:", result)


n = int(input())
delay_ms = int(input()) 
print("Waiting for", delay_ms, "milliseconds before calling square root function...")
time.sleep(delay_ms / 1000)
print("Calling square root function now...")
call_sqrt(n)

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

    

