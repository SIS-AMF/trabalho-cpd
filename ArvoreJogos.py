from NoJogo import NoJogo
from Jogo import Jogo


class ArvoreJogos:
    """Árvore binária de busca para armazenar jogos, ordenados por preço."""

    __raiz: NoJogo

    def __init__(self):
        self.__raiz = None

    def inserir(self, jogo: Jogo) -> None:
        novo_no = NoJogo(jogo)
        if self.__raiz is None:
            self.__raiz = novo_no
        else:
            self.__inserir_recursivo(self.__raiz, novo_no)

    def __inserir_recursivo(self, atual: NoJogo, novo_no: NoJogo) -> None:
        if novo_no.getJogo().getPreco() < atual.getJogo().getPreco():
            if atual.getEsquerda() is None:
                atual.setEsquerda(novo_no)
            else:
                self.__inserir_recursivo(atual.getEsquerda(), novo_no)
        else:
            if atual.getDireita() is None:
                atual.setDireita(novo_no)
            else:
                self.__inserir_recursivo(atual.getDireita(), novo_no)

    def buscarPorPreco(self, preco: float) -> list[Jogo]:
        return self.__buscar_recursivo(self.__raiz, preco)

    def __procuraIguais(self, atual: NoJogo, preco: float):
        if atual is None:
            return []
        if atual.getJogo().getPreco() == preco:
            return self.__procuraIguais(atual.getEsquerda(), preco) + [atual.getJogo()] + self.__procuraIguais(atual.getDireita(), preco)
        else:
            return []

    def __buscar_recursivo(self, atual: NoJogo, preco: float) -> list[Jogo]:
        if atual is None:
            return []
        if atual.getJogo().getPreco() == preco:
            return self.__procuraIguais(atual, preco)
        elif preco < atual.getJogo().getPreco():
            return self.__buscar_recursivo(atual.getEsquerda(), preco)
        else:
            return self.__buscar_recursivo(atual.getDireita(), preco)

    def buscarPorFaixaPreco(self, minimo: float, maximo: float) -> list[Jogo]:
        return self.__buscar_faixa(self.__raiz, minimo, maximo)

    def __buscar_faixa(self, atual: NoJogo, minimo: float, maximo: float) -> None:
        if atual is None:
            return []
        if atual.getJogo().getPreco() >= minimo and atual.getJogo().getPreco() <= maximo:
            return self.__buscar_faixa(atual.getEsquerda(), minimo, maximo) + [atual.getJogo()] + self.__buscar_faixa(atual.getDireita(), minimo, maximo)
        else:
            return []

    def preOrder(self) -> list[Jogo]:
        return self.__preOrder(self.__raiz)

    def __preOrder(self, no: NoJogo) -> list[Jogo]:
        if no is None:
            return []
        else:
            return self.__preOrder(no.getEsquerda()) + [no.getJogo()] + self.__preOrder(no.getDireita())
