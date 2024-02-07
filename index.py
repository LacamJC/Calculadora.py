## Calculadora em Python]

print('Escolha a operação desejada ( +, -, /, x)')
print("="*10)
print("= Digite 1 para ADIÇÃO")
print("= Digite 2 para SUBTRAÇÃO")
print("= Digite 3 para DIVISÃO")
print("= Digite 4 para MULTIPLICAÇÃO")
print("="*10)
user_choice = int(input('Qual sua escolha: '))

while user_choice > 4 or user_choice < 0:
    user_choice = int(input('Escolha inválida: '))

user_n1 = int(input('Primeiro valor : '))
user_n2 = int(input('Segundo valor : '))
res = 0

def switch(user_choice):
    if user_choice == 1:
        res = user_n1 + user_n2
        return res

    elif user_choice == 2:
        res = user_n1 - user_n2
        return res

    elif user_choice == 3:
        res = user_n1 * user_n2
        return res

    elif user_choice == 4:
        res = user_n1 / user_n2
        return res

# print(f'Operação escolhida {user_choice} resultado é {switch(user_choice)}')
operators = ['+','-','/','x']
print(f'{user_n1} {operators[user_choice]} {user_n2} = {switch(user_choice)}')
