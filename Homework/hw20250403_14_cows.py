n=0
print('Введите количество коров на лугу')
n=int(input())
if 5<= n <= 20 or n % 10 in [5, 6, 7, 8, 9, 0]:
    print('На лугу пасется', n, 'коров')
elif  n % 10 ==1:
    print('На лугу пасется', n, 'корова')
else:
    print('На лугу пасется', n, 'коровы') 
    