def get_area(largura:int, comprimento:int) -> float:
    area = largura * comprimento

    print(f'terreno {largura} x {comprimento}: area {area}')

largura:float = float(input('Largura: '))
comprimento:float = float(input('comprimento: '))

get_area(largura, comprimento)