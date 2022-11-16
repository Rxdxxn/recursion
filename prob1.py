def iterativ1(n):
    s=0
    for i in range(1,n+1):
        s+=(i*2*(i-1))
    return s

def recursiv1(n):
    if n<=1:
        return 0
    if n>1:
        return (n*2*(n-1))+recursiv1(n-1)

def iterativ2(n):
    s=0
    for i in range(1,n+1):
        s+=(i/((2*i-1)*(2*i+1)))
    return s

def recursiv2(n):
    if n==0:
        return 0
    if n>=1:
        return (n/((2*n-1)*(2*n+1)))+ recursiv2(n-1)

    
a=int(input("Dati un numar natural:"))
print("a)Suma este:",iterativ1(a))
print("a)Suma este:",recursiv1(a))
print("b)Suma este:",iterativ2(a))
print("b)Suma este:",recursiv2(a))


    