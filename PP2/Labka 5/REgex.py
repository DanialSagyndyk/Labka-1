import re

#EX1
str=input()
res=re.search("ab*",str)
print(res)

#EX2
str = input()
result = re.search(r"^[a][b]{2,3}+$",str)
print(result)

#EX3
str = input()
rsult = re.findall(r"[a-z]+_[a-z]+",str)
print(rsult)

#EX4
srt = input()
result = re.findall("^.*[A-Z]{1}[a-z]*+$",srt)
print(result)

#EX5
str = input()
result = re.search("^a+\w+b$",str)
print(result)

#EX6
str = input()
result  = re.sub(r"[ ,.]",":",str)
print(result)

#EX7
str = input()
result=re.sub(r"[_]","",str)
print(result)

#EX8
str = input()
result = re.split(r"[A-Z]",str)
print(result)

#EX9
str = input()
result = re.sub(r"(\b[A-Z][a-z]*\b)", r" \1",str)
print(result)

#EX10
str = input()
result = re.sub(r"[A-Z]", '_', str)
print(result)



