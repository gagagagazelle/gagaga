#　空配列の作成　[]
#empty_list1 = []
#print(empty_list1)
#
#
## リスト作成 []
#str_list1 = ['A','B','C']
#print(str_list1)
#
##　空配列の作成　list()
#empty_list2 = list()
#print(empty_list2)
#
## リスト作成 list()
#str_list2 = list(['A','B','C'])
#print(str_list2)
#
#a=list('ABC')
#print("a =",a)

#tuple_sample=('A','B','C')
#print(tuple_sample)
#print(list(tuple_sample))

#today = '2018.06.13'
#print(today.split('.'))
#print(today.split('.')[-1])
#print(today.split('.')[5])

prime = [2,3,5,7,]
not_prime = [1,4,6,8,9]
all_number = [prime,not_prime]
#print(all_number)
#print(all_number[0])
#print(all_number[0][0])
all_number[0][0] = 11
print(all_number)
print(all_number[::-1])
all_number.append([100,200])
print(all_number)
print(all_number[0:2])
all_number.insert(1,[765])
print(all_number)
del all_number[0]
print(all_number)
all_number.remove([765])
print(all_number)
print([765] in all_number)
s=['a','b','c']
print(','.join(s))
