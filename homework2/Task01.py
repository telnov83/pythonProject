# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

number_off_month = int(input('Введите номер месяца: '))
if number_off_month < 1 or number_off_month > 12:
    print('такого месяца не существует')
    exit()
number = str(number_off_month)
pora_goda = [['12', '1', '2'], ['3', '4', '5'], ['6', '7', '8'], ['9', '10', '11']]
winter = ['12', '1', '2']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']
for i in pora_goda:
    for j in i:
        if number == j:
            if i == winter:
                print('это зима')
                break
            elif i == spring:
                print('это весна')
                break
            elif i == summer:
                print('это лето')
                break
            elif i == autumn:
                print('это осень')
                break
number_off_month = int(input('Введите номер месяца: '))
number = str(number_off_month)
slovar = {}
slovar['winter'] = '12,1,2'
slovar['spring'] = '3,4,5'
slovar['summer'] = '6,7,8'
slovar['autumn'] = '9,10,11'

for i in slovar.keys():
    if number in slovar[i]:
        print(i)
