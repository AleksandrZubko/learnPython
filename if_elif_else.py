'''
x = 10
if x % 2 == 0:
   print('чётное')
elif x % 2 != 0:
   print('нечётное')
else:
   print('чёртишо')
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
