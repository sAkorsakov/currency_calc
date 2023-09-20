# 1. Приветствие
# 2. Мануал - *** как пользоваться программой * какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Сколько у вас исходной валюиы
# 6. Подсчёт
# 7. Вывод результатов


print('Конвертер валют')

# 2
print('''
Инструкция:
1. Ввести исходную валюту
2. Ввести конечную валюту
3. Скоко у вас исходной валюты
''')

import requests

URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_foEom5anFTna47zJnBIEtHgihVgpgG7SI565Gskj&currencies="
# API_KEY = "fca_live_foEom5anFTna47zJnBIEtHgihVgpgG7SI565Gskj"

def get_actual_currencies():
    response = requests.get(URL)  # api_key уже в юрл поэтому не плюсую апи_кии
    data_currency = response.json()
    return data_currency


CURRENCIES = dict(get_actual_currencies())
CURRENCIES = (CURRENCIES['data'])

# print(CURRENCIES)
print('Доступные валюты:')
for key in CURRENCIES:
    print(f'* {key}')


def check_input_currency(currency):
    check_currency = False
    while not check_currency:
        if currency in CURRENCIES.keys():
            return currency
        else:
            currency = input("Укажите валюту в соотвествии со списком выше: ")


current_currency = input("Введите исходную валюту: ")
current_currency = check_input_currency(current_currency)
result_currency = input("Введите требуемую валюту: ")
result_currency = check_input_currency(result_currency)
amount_current = float(input("Введите количество исходной валюты: "))


# 6
def converter(amount, from_currency, to_currency):
    current_value = CURRENCIES.get(from_currency)
    result_value = CURRENCIES.get(to_currency)
    amount_result = round(result_value * float(amount) / current_value, 2)
    return amount_result


amount_result = converter(float(amount_current), current_currency, result_currency)
print(f'{amount_current} {current_currency} = {amount_result} {result_currency}')
