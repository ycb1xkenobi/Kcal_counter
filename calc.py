# gender = input('enter ur gender (м/ж): ')
# age = int(input('enter ur age: '))
# weight = int(input('enter ur weight (kg)'))
# height = int(input('enter ur height (cm)'))
# kf = float(input('Введите уровень активности:\n Минимальный уровень активности — 1.2,\n Низкий уровень активности — 1.375,\nСредний уровень активности — 1.55,\n Высокий уровень — 1.725,\n Очень высокий —  1.9:\n'))
# mode = int(input('Введите мод:\n 1 - похудение \n2 - поддержание суточной нормы \n3 - набор массы'))
import sqlite3

message_text = ''

con = sqlite3.connect("food.db")
cur = con.cursor()

def Find_BMR(gender, age,weight, height):
    if (gender == 'м'):
        bmr = 88.362 + (13.4 * weight) + (4.8 * height) - (5.677 * age)
    elif (gender == 'ж'):
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        print('error has happend')
    return bmr
def Find_BMR_mode(bmr, mode):
    if (mode == 1):
        bmr_mode = bmr*0.85
    elif (mode == 2):
        bmr_mode = bmr
    elif (mode == 3):
        bmr_mode = bmr*1.2
    return bmr_mode
def Day_kcal(gender, age, weight, height, mode):
    bmr = Find_BMR(gender, age, weight, height)
    bmr_mode = Find_BMR_mode(bmr, mode)
    message_text = ''
    if (mode == 1):
        message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
        # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
        message_text = message_text + f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},\n'
        # print(f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},')
        if (weight*0.7 <= 30):
            message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
            # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
        else:
            message_text = message_text + f'{weight} г жиров в день'
            # print(f'{weight} г жиров в день')
        message_text = message_text + f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
        # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')


    if (mode == 2):
        message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
        # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
        message_text = message_text + f'не менее {weight * 0.75:.1f}-{weight} г белков в день, оптимально {weight * 1.5}-{weight * 2},\n'
        # print(f'не менее {weight*0.75:.1f}-{weight} г белков в день, оптимально {weight*1.5}-{weight*2},')
        if (weight*0.7 <= 30):
            message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
            # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
        else:
            message_text = message_text + f'{weight} г жиров в день'
            # print(f'{weight} г жиров в день')
        message_text = message_text + f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
        # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')


    if (mode == 3):
        message_text = message_text + f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,\n'
        # print(f'советуем употреблять примерно {bmr_mode:.1f} ккал в день,')
        # print(f'не менее {weight*1.5:.1f}-{weight*2} г белков в день, оптимально {weight*2.5}-{weight*3},')
        message_text = message_text + f'не менее {weight * 0.75:.1f}-{weight} г белков в день, оптимально {weight * 1.5}-{weight * 2},\n'
        if (weight*0.7 <= 30):
            message_text = message_text + f'не менее 30 г жиров в день но не более {weight*2} г жиров в день\n'
            # print(f'не менее 30 г жиров в день но не более {weight*2} г жиров в день')
        else:
            message_text = message_text + f'{weight} г жиров в день'
            # print(f'{weight} г жиров в день')
        message_text = message_text + f' и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных'
        # print(f'и примерно {bmr_mode*0.4/4:.1f}-{bmr_mode*0.5/4:.1f} г углеводов, желательно не менее {bmr_mode*0.3/4:.1f}-{bmr_mode*0.4/4:.1f} из них сложных')
    return message_text


def Search_name(a):
    s = []
    s.append(a)
    f = (a.split(' '))

    for x in f: s.append(x)
    for i in range(len(s)):
        if len(s[i]) >= 4 and (s[i][-1] == 'а' or s[i][-1] == 'и' or s[i][-1] == 'ы'):
            s[i] = s[i][:len(s[i]) - 1]

    for x in s:
        print(x)
        sql = f"SELECT * FROM food WHERE name LIKE '%{x}%'"
    cur.execute(sql)
    return (cur.fetchall())
