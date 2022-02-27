#1

import random

chislo_1 = random.randint(1,10)
while True:
    chislo_2 = int(input("Введите число от 1 до 10 "))
    if chislo_1 == chislo_2 :
        print("Вы угадали!")
        break
    else:
        if chislo_2 > chislo_1:
            print("Введённое число больше загаданного! Попробуйте еще раз")
        else:
            print("Введённое число меньше загаданного! Попробуйте еще раз")

#2

def password_1()->str:
    import random
    length = random.randint(7,10)
    password_2 = ' '
    for i in range(length + 1):
        password_2 += chr(random.randint(33,126))
    return password_2
print(password_1())

#3

def check_password(password: str)->bool:
    sum_upper = sum(map(str.isupper, password))
    sum_lower = sum(map(str.islower, password))
    sum_digit = sum(map(str.isdigit, password))
    if len(password) >= 8 and sum_upper > 0 and sum_lower > 0 and sum_digit > 0:
        return True
    else:
        return False
print(check_password(input('Введите пароль ')))

#4

import random

def password_1():
  password_2 = []
  for i in range(random.randint(7,10)-1):
    password_2.append(chr(random.randint(33,126)))
  return  ''.join (password_2)

def checking(passw):
  return len(passw) >= 8 and passw.lower() != passw and passw.upper() != passw  and any(char.isdigit() for char in passw)

count = 0
while True:
  p = password_1()
  if checking(p) == True:
    print(f"Надежный пароль: {p},   количество попыток: {count}")
    break
  else:
     count += 1
