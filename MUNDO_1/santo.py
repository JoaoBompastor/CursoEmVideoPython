#ler se uma cidade comeca ou nao com santo

cidade = str(input('em que cidade voce nasceu? ')).strip()
cidadeupper = cidade.upper()

print(cidadeupper.startswith('SANTO'))