# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
#          "Ты ввёл int (Валюта)"
#          "Конвертированная сумма в USD = int"
#          "Конвертированная сумма в EUR = int"
#          "Конвертированная сумма в CHF = int"
#          "Конвертированная сумма в GBP = int"
#          "Конвертированная сумма в CNY = int"
# 3. Валюту пользователя определите сами.
eur_item = 'eur'
uah_eur_rate = 32.06
uah_item = 'uah'
uah_usd_rate = 28.37
chf_item = 'chf'
uah_chf_rate = 31.12
gbp_item = 'gbp'
uah_gbp_rate = 38.25
cny_item = 'cny'
uah_cny_rate = 4.48
currency_convertor = True

if currency_convertor:
    target_currency = uah_item
    currency_result = 0
    target_currency_amount = input('Введите сумму гривен : ')
    print('Вы ввели', target_currency_amount, 'гривен')

    if target_currency == 'uah':
        currency_result = int(target_currency_amount) / uah_usd_rate
        print('Конвертированная сумма в USD',  '=', round(currency_result, 2))
        currency_result = int(target_currency_amount) / uah_eur_rate
        print('Конвертированная сумма в EURO', '=', round(currency_result, 2))
        currency_result = int(target_currency_amount) / uah_chf_rate
        print('Конвертированная сумма в CHF', '=', round(currency_result, 2))
        currency_result = int(target_currency_amount) / uah_gbp_rate
        print('Конвертированная сумма в GBR', '=', round(currency_result, 2))
        currency_result = int(target_currency_amount) / uah_cny_rate
        print('Конвертированная сумма в CHY', '=', round(currency_result, 2))