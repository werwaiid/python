#5
import random

spisok = input("Введите слова ").split(' ')
word = spisok[random.randint(0, len(spisok) - 1)]
spisok_new = list(word)
n = random.randint(0, len(spisok_new) - 1)
b = spisok_new[n]
spisok_new[n] ="?"
print("Угадайте букву " + ''.join(spisok_new))
bukva = input("Введите букву ")
if b == bukva:
    print("Победа")
else:
    print("Увы! Попробуте в другой раз!")
print("Слово " + word)

#6
text =  """В тот год осенняя погода
Стояла долго на дворе
Зимы ждала ждала природа
Снег выпал только в январе
На третье в ночь Проснувшись рано
В окно увидела Татьяна
Поутру побелевший двор
Куртины, кровли и забор
На стеклах легкие узоры
Деревья в зимнем серебре
Сорок веселых на дворе
И мягко устланные горы
Зимы блистательным ковром
Все ярко, все бело кругом"""

print("Количество строк ",len(text.split("\n")))
s = 0
for i in text.split("\n"):
    s += len(i.split(" "))
print("Количество слов ",s)
