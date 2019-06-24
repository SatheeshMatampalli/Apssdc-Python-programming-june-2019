# def isspecial(n,p):
#     if primefactors(n)>=p:
#         return True
#     return False
def primeNo(n):
    fc = 0
    for k in range(1,n+1):
        n = k
        c = 0
        for i in range(1,n+1):
            if(n%i==0):
                c=c+1
        if(c==2):
            fc = fc+1
    if (fc==2):
        print("YES")
    else:
        print("NO")

# primeNo(7)
# def primefactors(n):
#     if primeNo(n):
#         return 1
#     count=0
#     for i in range(2,n//2+1):
#         if primeNo(i) and n%i==0:
#             count=count+1
#     return count
# isspecial(30,2)