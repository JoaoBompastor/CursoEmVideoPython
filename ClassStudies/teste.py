from time import sleep
from playsound import playsound

class Bottle:

    # self method, so no staticmethod
    def Fill(self):
        print('Filling...')
        sleep(2)

    # no self method, so staticmethod
    @staticmethod
    def Pour():
        print('Pouring...')
        sleep(2)
        playsound('TESTE/testepy/AssobioWhatsApp.mp3')

    # no self method, so staticmethod
    @staticmethod
    def Adicionar_Um(Numero:int) -> int:
        return Numero + 1

Garrafa = Bottle()

Garrafa.Fill()
Garrafa.Pour()
print(Garrafa.Adicionar_Um(10))