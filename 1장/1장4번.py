def gcd(a,b):
    print("gcd",(a,b))
    while b !=0:
        r=a%b
        a=b
        b=r
    return a
gcd(60,28)
gcd(28,4)
gcd(4,0)

print("60과 28의 최대 공약수 =",gcd(60,28))
print()