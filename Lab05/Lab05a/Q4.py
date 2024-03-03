#Q4.1
tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#Q4.2
tuple2 = (10,20,30,40)
a,b,c,d = tuple2
print(a)
print(b)
print(c)
print(d)

#Q4.3
tuple11 = (11,22)
tuple22 = (99,88)
tuple11, tuple22 = tuple22,tuple11
print('tuple1:',tuple11)
print('tuple2:',tuple22)
