# ate 9: mirim, ate 14: infantil, ate 19: junior, ate 25: senior, acima de 25: master

ANO_NASCIMENTO = int(input('digite o ano de nascimento do atleta: '))
ANO_ATUAL = 2023
IDADE = 2023 - ANO_NASCIMENTO

if IDADE <= 9:
    print('MIRIM, {} anos' .format(IDADE))

elif 10 <= IDADE <= 14:
    print('INFANTIL, {} anos' .format(IDADE))

elif 15 <= IDADE <= 19:
    print('JUNIOR, {} anos' .format(IDADE))

elif 20 <= IDADE <= 25:
    print('SENIOR, {} anos' .format(IDADE))

else:
    print('MASTER, {} anos' .format(IDADE))
