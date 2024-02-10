import datetime
import random
'''
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
'''
#EX3
def remove_microseconds(date):
    return date.replace(microseconds = 0)


date = datetime.datetime.now()
remov = remove_microseconds(date)

print(remov)



