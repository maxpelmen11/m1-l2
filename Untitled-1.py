import random

def rp():
    x = int(input('Количество паролей?' + '\n'))
    y = int(input('Длина пароля?' + '\n'))
    sm = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for A in range(x):
        pas = ''
        for B in range(y):
            pas += random.choice(sm)
        print(pas)

def ep():
    v = int(input('Number of passwords?' + '\n'))
    u = int(input('Password length?' + '\n'))
    m = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for D in range(v):
        pas2 = ''
        for Q in range(u):
            pas2 += random.choice(m)
        print(pas2)

lang = input('ru/eng?')

if lang == "ru" or lang == 'RU':
    rp()
elif lang == 'eng' or lang == 'ENG':
    ep()
else:
    print ('ОШИБКА/ERROR')
    