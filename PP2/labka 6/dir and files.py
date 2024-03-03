import os
'''
#EX1
text=input("Write the path to dir ")
folders=os.listdir(ex)
for i in folders:
    print(i,end=" ")
#EX2
def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path {path} does not exist")
        return
    if os.access(path, os.R_OK):
        print(f"Read access to the path {path} is granted")
    else:
        print(f"No read access to the path {path}")
    if os.access(path, os.W_OK):
        print(f"Write access to the path {path} is granted")
    else:
        print(f"No write access to the path {path}")

    if os.path.isdir(path):
        if os.access(path, os.X_OK):
            print(f"Execute access to the path {path} is granted")
        else:
            print(f"No execute access to the path {path}")
    else:
        print(f"The path {path} is not a directory")

path_to_check = "write the path to dir"

check_path_access(path_to_check)
#EX3
text=input("Write the path to dir ")
if os.path.exists(text):
    print("It exists")
    print(os.path.basename(text))
    print(os.path.dirname(text))
else:
    print("It doesn't exist")
'''
#EX4
file=open("example.txt","r")
cnt=0
for i in file:
    cnt+=1
print(cnt)
file.close()
#ex5
file=open("example2.txt","w")
n=int(input())
s=0
smm=list()
for i in range(n):
    s=int(input())
    smm.append(s)
file.write(str(smm))
print("check example2.txt")
file.close()
#ex6
for i in range(26):
    file=chr(ord('A') + i)+".txt"
    open_file=open(file,"w")

#ex7
file = open("example2.txt","r")
file1 = open("example.txt","a")
for i in file:
    file1.write(i)
file.close()
file1.close()
#Ex8
ex=input()
if os.path.exists(ex):
    print("Yes exists")
    os.remove(ex)
else:
    print("This path is not correct")


