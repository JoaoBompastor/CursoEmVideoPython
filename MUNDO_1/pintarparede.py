#pintar uma porra de uma parede 

altura = float(input('qual eh a altura da parede? '))
largura = float(input('qual eh a largura da parede? '))
print('a area da sua parede eh {:.3f}, e serao necessarios {:.4f} litros de tinta' .format(largura * altura, (largura * altura) / 2))