import random

l="abcdefghijklmnopqrstuvwxyz"
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="0123456789"
s="{}[]@*._/,"
a=l+u+n+s
length=12
pwd="".join(random.sample(a,length))
print(pwd)
