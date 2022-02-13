'''
x = 10
if x % 2 == 0:
   print('чётное')
elif x % 2 != 0:
   print('нечётное')
else:
   print('чёртишо')
'''

'''
A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
   print('Это нормально')
elif H < A:
   print('Недосып')
elif H > B:
   print('Пересып')
'''

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')
