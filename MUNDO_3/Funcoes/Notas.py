def Notas(*notas, situacao: bool = False) -> dict:
    media = 0
    dicionario: dict = {}
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)

    for nota in notas:
        media += nota

    dicionario['media'] = media / len(notas)

    if situacao == True:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'Boa'

        else:
            dicionario['situacao'] = 'Abaixo da media'

    return dicionario

        
# main
resp = Notas(7, 7, 7, situacao= False)
print(resp)