from Jogo import Jogo


class NoJogo:
    __jogo: Jogo
    __esquerda: float
    __direita: float

    def __init__(self, jogo: Jogo):
        self.__jogo = jogo
        self.__esquerda = None
        self.__direita = None

    # Getters

    def getJogo(self):
        return self.__jogo

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    # Setters

    def setDireita(self, direita: float):
        self.__direita = direita

    def setEsquerda(self, esquerda: float):
        self.__esquerda = esquerda
