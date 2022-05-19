help_message = '''
Отправьте команду /buy, чтобы перейти к покупке.
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Здравствуйте, вас привествует магазин "JetStreetSam".Желаете приобрести игровую приставку Playstation 4?"!\n' + help_message

terms = '''\
Информацию по достваке вам вышлют на почту после плотежа!
'''

item_title = 'PS 4'
item_description = '''\
Купить PS4 
'''

AU_error = '''\
В данную страну доставка не оформляется.
'''


successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!  
Данные вашей доставки вышлены вам на почту'''



MESSAGES = {
    'start': start_message,
    'help': help_message,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}
