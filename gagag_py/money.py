money_name = ["一万円札","五千円札","千円札","五百円玉","百円玉","五十円玉","十円玉","五円玉","一円玉"]
money_count = [0 for x in range(len(money_name))]
#print(money)

print('金額入力>>')
price = int(input())
payment = int(10000)
otsuri = payment - price
otsuri_name = []

while otsuri != 0:
    while otsuri >= 5000:
        otsuri -= 5000
        otsuri_name.append(5000)
    while otsuri >= 1000:
        otsuri -= 1000
        otsuri_name.append(1000)
    while otsuri >= 500:
        otsuri -= 500
        otsuri_name.append(500)
    while otsuri >= 100:
        otsuri -= 100
        otsuri_name.append(100)
    while otsuri >= 50:
        otsuri -= 50
        otsuri_name.append(50)
    while otsuri >= 10:
        otsuri -= 10
        otsuri_name.append(10)
    while otsuri >= 5:
        otsuri -= 5
        otsuri_name.append(5)
    while otsuri >= 1:
        otsuri -= 1
        otsuri_name.append(1)

#print(otsuri_name)
money_count[1] = otsuri_name.count(5000)
money_count[2] = otsuri_name.count(1000)
money_count[3] = otsuri_name.count(500)
money_count[4] = otsuri_name.count(100)
money_count[5] = otsuri_name.count(50)
money_count[6] = otsuri_name.count(10)
money_count[7] = otsuri_name.count(5)
money_count[8] = otsuri_name.count(1)

money = [money_name,money_count]

for i in range(len(money_name)):
    if money_count[i] != 0:
        print(money[0][i],"",money[1][i])
