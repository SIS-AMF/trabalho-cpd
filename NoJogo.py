from Jogo import Jogo


class NoJogo:
    """Representa um nó da árvore binária de jogos."""

    __jogo: Jogo
    __esquerda: "NoJogo"
    __direita: "NoJogo"

    def __init__(self, jogo: Jogo):
        self.__jogo = jogo
        self.__esquerda = None
        self.__direita = None

    # Getters
    def getJogo(self) -> Jogo:
        return self.__jogo

    def getEsquerda(self) -> "NoJogo":
        return self.__esquerda

    def getDireita(self) -> "NoJogo":
        return self.__direita

    # Setters
    def setEsquerda(self, esquerda: "NoJogo") -> None:
        self.__esquerda = esquerda

    def setDireita(self, direita: "NoJogo") -> None:
        self.__direita = direita
