import datetime
#EX1
x = datetime.datetime.now()
y = x - datetime.timedelta(days = 5)

print(y.strftime("%A"))

#EX2
y = datetime.datetime.now()
q = y - datetime.timedelta(days=1)
z = y + datetime.timedelta(days=1)

print(q.strftime("%x"))
print(z.strftime("%x"))

#EX3
date = datetime.datetime.now()
remov = date.replace(microsecond=0)
print(remov)

#EX4
import datetime
today=datetime.datetime.now()
few=int(input())
some=today.replace(day=few)
between=today.day - some.day
print(between)
print(between*24*60*60)




