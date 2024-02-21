import math
import itertools

#EX1
def pow(n):
  for i in range(n+1):
    yield i**2

n = int(input())
k = pow(n)
for i in  k:
  print(i)
  
#EX2
def zhup(n):
  for i in range(n+1):
    if i%2==0:
      yield i

n = int(input())
answer = zhup(n)
for i in answer:
  print(i,end=" ")
  
#EX3

def ex3(n):
  for i in range(0,n+1):
    if i %3 == 0 or i %4 == 0:
      yield i
      
n = int(input())
answe = ex3(n)
for i  in answe:
  print(i)
  
#EX4

def squares(a,b):
  for i in range(a,b+1):
    yield i**2
    
answer = squares(int(input()),int(input()))
for i in answer:
  print(i,end=" ")
  
#EX5
def zero(n):
  while n>=0:
    yield n
    n-=1
answeer  = zero(int(input()))
for i in answeer:
  print(i,end=" ")  
  