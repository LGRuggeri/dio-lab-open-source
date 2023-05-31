"""Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno_de_estudo= input('Qual turno de estudo M-Matutino, V-Vespertino ou N-Noturno: ')

if turno_de_estudo == 'm' or turno_de_estudo == 'M':
    print('Você estuda no turno Matutino:')
elif turno_de_estudo == 'v' or turno_de_estudo == 'V':
    print('Você estuda no turno Vespertino')
elif turno_de_estudo == 'n' or turno_de_estudo == 'N|':
    print('Você estuda no turno Noturno:')
else:
    print('Turno inválido!!!')