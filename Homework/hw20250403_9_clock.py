print('Введите количество прошедших минут от 1 до 106')
minutes=int(input())
if minutes < 0 or minutes > 106:
    print('Количество минут не удовлетворяет условиям задачи')
else:
    print('Часы показывают', minutes // 60, minutes % 60)