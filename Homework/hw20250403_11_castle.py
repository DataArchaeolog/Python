hole=[]
brick=[]
print('Введите ширину отверстия')
hole.append(float(input()))
print('Введите высоту отверстия')
hole.append(float(input()))
print('Введите высоту кирпича')
brick.append(float(input()))
print('Введите ширину кирпича')
brick.append(float(input()))
print('Введите толщину кирпича')
brick.append(float(input()))
if sorted(hole)[0] >= sorted(brick)[0] and sorted(hole)[1] >= sorted(brick)[1]:
    print('Кирпич пролезет')
else:
    print('Кирпич не пролезет')