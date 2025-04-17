print('Количество студентов')
students=int(input())
print('Количество яблок')
apples=int(input())
if (apples > 10000) or (students > 10000) or (apples < 0) or (students <= 0):
    print('Количество яблок или студентов не удовлетворяют условиям задачи')
else:
    print('Осталось яблок:',apples % students, 'Каждый студент получил яблок:', apples // students)