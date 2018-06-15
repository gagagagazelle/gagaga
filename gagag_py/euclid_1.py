print("整数二つ入力")
a,b = int(input()),int(input())

#ユークリッドの互除法
def gcd(a,b):
    if b == 0:
        return a
    else:
        #print("b=",b,"\na%b=",a%b)
        return gcd(b,a%b)

#モード選択（最大公約数or最小公倍数）
print("最大公約数を求める場合は 0\n最小公倍数を求める場合は 1\nを入力")
c = int(input())

def modeinput(c):
    if c == 0 or c == 1:
        return c
    else:
        print("0または1じゃない、再入力")
        c = int(input())
        return modeinput(c)

modeinput(c)

if c == 0:
    print("answer =",gcd(a,b))
else:
    print("answer =",a*b/gcd(a,b))
