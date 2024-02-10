#EX1
def Ounces():
    x = int(input())
    ounc=x/28.3495231
    return ounc
    
Ounces()

#EX2
def Temperature():
    Far = int(input())
    C = (5/9)*(Far-32)
    return C
    
Temperature()

#EX3
def solve(x,y):
    x = int(input())
    y = int(input())
    p = x*2
    len = y - p
    t = len/2
    print(x - t, t)
    
        
solve('x','y')

#Ex4
 
def filter_prime(x): 
    for y in x: 
        print("Primes=",y," ") 
n=int(input("Write length ")) 
my=list() 
primes=list() 
while n>0: 
    t=int(input()) 
    my.append(t) 
    n-=1 
for i in my: 
    count = 0 
    for j in range(1,i): 
        if i%j==0: 
            count+=1 
    if count==1: 
        primes.append(i) 


filter_prime(primes)
  

#Ex5
import itertools
def permuta():
    for i in permutation:
        print(i)
string=str(input())
permutation = list(itertools.permutations(string))
permuta()

#Ex6

def reverse():
    string2=x[::-1]
    for i in string2:
        print(i,end=" ")
string1=str(input())
x=string1.split()
reverse()


#Ex7
def has_33(nums):
    pass
    bool = True
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]==3:
            return True
            
    return False
            

res1 = has_33([1, 3, 3])
res2 = has_33([1, 3, 1, 3])
res3 = has_33([3, 1, 3])

print(res1)
print(res2)
print(res3)

#EX8

def spy_game(nums):
    pass
    list0 = False
    list0_0 = False
    for i in nums:
        if i == 0 and not list0:
            list0 = True
        elif i==0 and list0 and not list0_0:
            list0_0 = True
        elif i == 7 and list0_0:
            return True
        
    return False
            
             
resul1 = spy_game([1,2,4,0,0,7,5])
resul2 = spy_game([1,0,2,4,0,5,7])
resul3 = spy_game([1,7,2,0,4,5,0])

print(resul1)
print(resul2)
print(resul3)
    
#Ex9

import math
def ex_9():
    x = int(input())
    V = 4/3*3,14*math.pow(x,3)
    return V

ex_9()

#EX10

def unique(nums):
    list1=list()
    for i in range(0,10):
        list1.append(0)
    for i in nums:
        list[i]+=1
    cnt=0
    for i in list1:
        if i>=1:
            list2.append(cnt)
        cnt+=1
    print(list2)
x=int(input())
mylist=list()
while(x>0):
    a=int(input())
    mylist.append(a)
    x-=1
list2=list()

unique(mylist)


#Ex11

def polindrom():
    st = str(input())
    ex = st[::-1] 
    if st==ex:
        print("palindrome")
    else:
        print("No palindrome")
        
polindrom()
#EX12
def histogram(numbers):
    for num in numbers:
        bar = '*' * num
        print(bar)

numbers_list = [4,9,7]
histogram(numbers_list)



#Ex13
import random
def Guess_the_number():
    print("Hello! What is your name?")
    print("KBTU")
    x = random.randint(1,20)
    i = 1
    while i < 20*2:
        print("Well, KBTU, I am thinking of a number between 1 and 20.")
        print("Take a guess.")
        y = random.randint(1,20)
        print(y)
        if x == y:
            print("Good job, KBTU! You guessed my number in", i ,"guesses!")
            break
        i += 1
     
Guess_the_number()   
