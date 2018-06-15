print("整数二つ入力")
a,b = int(input()),int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        #print("b=",b,"\na%b=",a%b)
        return gcd(b,a%b)
print("answer =",gcd(a,b))
