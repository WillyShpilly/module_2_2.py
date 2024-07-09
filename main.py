first = int(input('Введите значение 1:'))
second = int(input('Введите значение 2:'))
third = int(input('Введите значение 3:'))
if first == second and first == third and second == third:
    print("3")
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')