# mas=[1,2,3,4,5,6,7,8,9,78,5,4,3,3,4,5,4,23,2,3,45,65,6]
# for i in range(0,len(mas),2):
#     print(mas[i])

# mas=[1,2,3,4,5,6,7,8,9,78,5,4,3,3,4,5,4,23,2,3,45,65,6]
# for i in range(0,len(mas)):
#     if not mas[i] % 2:
#         print(mas[i])


# mas=[1,2,3,4,5,6,7,8,9,78,5,4,3,3,4,5,4,23,2,3,45,65,6]
# for i in range(1,len(mas)):
#     if mas[i] > mas[i-1]:
#         print(mas[i])


# mas=[1,2,-3,4,5,6]#,-7,8,9,-78,-5,-4,3,-3,4,5,4,23,2,3,45,65,6]
# print(len(mas))
# for i in range(1,len(mas)-1):
#     if (mas[i-1]>=0 and mas[i+1]>=0) or (mas[i-1]<0 and mas[i+1]<0):
#         print(mas[i])

# mas=[1,2,-3,4,5]#,6,-7,8,9,-78,-5,-4,3,-3,4,5,4,23,2,3,45,65,6]
# print(mas)
# minn=0
# maxx=0
# for i in range(len(mas)):
#     if mas[i]>mas[maxx]:
#         maxx=i
#     elif mas[i]<mas[minn]:
#         minn=i
# tmp=mas[minn]
# mas[minn]=mas[maxx]
# mas[maxx]=tmp
# print(mas)
#------------------------------ДЗ к 7 апреля ---------------------------------------------------------
# Шеренга по росту
# mas=[175,173,173,170,165,165,163,159,157,156,155,145]
# print('Введите рост Пети')
# rost_p=int(input())
# for i in range(len(mas))[::-1]:
#     if rost_p<=mas[i]:
#          print('Номер Пети в строю',i+2)
#          break
#     else:
#          if i==0:
#             print('Номер Пети в строю',1)

# Вывод уникальных элементов
# mas=[175,173,173,170,165,165,163,159,157,156,155,145]
# flag=0
# print('Уникальные элементы')
# for i in range(len(mas)):
#     for k in range(len(mas)):
#         if (mas[i]==mas[k]) and (i != k):
#             flag=1
#     if flag == 0:
#         print(mas[i])
#     flag=0

# Сжатие списка
mas=[175,173,0,173,0,170,165,0,0,165,163,0,159,157,156,155,145]
zero_counter=0
i=0
n=len(mas)
while i < n:
    if mas[i]==0:
        mas.pop(i)
        n -=1
        zero_counter +=1
    else:
        i +=1    
for k in range(zero_counter):
    mas.append(0)
for z in range(len(mas)):
    print(mas[z])
