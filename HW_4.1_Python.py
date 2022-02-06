# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
#       "Ты ввёл int (Валюта)"
#       "конвертированная сумма в USD = int"
# 3. Валюту пользователя определите сами.

uah_item = 'uah'
uah_usd_rate = 28.37
currency_convertor = True

if currency_convertor:
    target_currency = uah_item
    currency_result = 0
    target_currency_amount = input('Введите сумму гривен : ')

    if target_currency == 'uah':
        print('Вы ввели', target_currency_amount, 'гривен')
        currency_result = int(target_currency_amount) / uah_usd_rate
        print('Конвертированная сумма в usd',  '=', round(currency_result, 2))

