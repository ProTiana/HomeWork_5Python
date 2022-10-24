# Игра с конфетами для 2х игроков
import random

count_of_sweets = 2021
gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
random_start = random.randint(1, 2)
# print (random_start)
if random_start == 1:
    current_gamer = gamer_1
else:
    current_gamer = gamer_2
while count_of_sweets > 0:
    print('количество оставшихся конфет: {}'.format(count_of_sweets))
    while True:
        number_to_delete = int(input('ход игрока {} (1 - 28): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 28: break
        else: print('Ошибка. Игрок может взять от 1 до 28 конфет. Повторите попытку.')

    count_of_sweets -= number_to_delete
    current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

print('Победил {}'.format(current_gamer))
