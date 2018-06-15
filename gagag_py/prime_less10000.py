from math import sqrt
import time

print("0~3を入力してモード選択(3が一番いいやり方)")
c = int(input())

def modeinput(c):
    t1 = time.time()
    if c >= 0 and c <= 3:
        return c
    else:
        print("0~3じゃない、再入力")
        c = int(input())
        return modeinput(c)
    t2 = time.time()
    elapsed_time = t2 - t1
    print(f"経過時間:{elapsed_time}")
modeinput(c)

if c==0:
    for i in range(2,10000):
        if 0 not in [i%j for j in range(2,int(i/2+1))]:
            print(i)
elif c==1:
    t1 = time.time()
    for i in range(2,10000):
        if 0 not in [i%j for j in range(2,int(sqrt(i))+1)]:
            print(i)
    t2 = time.time()
    elapsed_time = t2 - t1
    print(f"経過時間:{elapsed_time}")
elif c==2:
    t1 = time.time()
    MAX = 10000
    LIST = range(2,MAX+1)
    for i in range(2,int(MAX**0.5)):
        LIST = [x for x in LIST if (x == i or x % i != 0)]
    for j in LIST:
        print(j)
    t2 = time.time()
    elapsed_time = t2 - t1
    print(f"経過時間:{elapsed_time}")
else:
    t1 = time.time()
    #エラトステネスの篩
    #（コードは煩雑そうに見えるが、速度が圧倒的に速い。
    #　大きな数までの素数表が必要な場合に必要な方法。）
    a = list()
    for i in range(0,10000):
        a[i] = i
    a[1] = 0 # 1 は素数ではない
    for p in a:
        if not p:
            continue
        elif p > 100: # 100 = sqrt(10000)
            break
        else:
            for multi in xrange(p+p, 10000, p):
                a[multi] = 0

    # この時点で、aは、素数p番目にはpが、それ以外には0が入ったリストになっている。
    a = [x for x in a if x]
    for x in a:
        print(x)

    t2 = time.time()
    elapsed_time = t2 - t1
    print(f"経過時間:{elapsed_time}")
