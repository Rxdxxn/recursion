from random import randint as ran

def CMMDC(m,n):
    if m>n:
        return CMMDC(m-n,n)
    if n>m:
        return CMMDC(m,n-m)
    if m==n:
        return m

a=ran(1,100)
b=ran(1,100)
print("Valoarea lui a:",a)
print("Valoarea lui b:",b)
print("Cel mai mare divizor comun dintre a si b:",CMMDC(a,b))
