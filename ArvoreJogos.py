from NoJogo import NoJogo
from Jogo import Jogo


class ArvoreJogos:
    __raiz: Jogo

    def __init__(self):
        self.__raiz = None

    def inserir(self, jogo: Jogo):
        '''Inserir um jogo na árvore'''
        novo_no = NoJogo(jogo)
        if self.__raiz is None:
            self.__raiz = novo_no
        else:
            self.__inserir_recursivo(self.__raiz, novo_no)

    def __inserir_recursivo(self, atual: NoJogo, novo_no: NoJogo):
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

    def buscarPorPreco(self, preco: int):
        '''Buscar jogos por preço exato'''
        return self.__buscar_recursivo(self.__raiz, preco)

    def __buscar_recursivo(self, atual: NoJogo, preco: int):
        if atual is None:
            return []
        if atual.getJogo().getPreco() == preco:
            return [atual.getJogo()]
        elif preco < atual.getJogo().getPreco():
            return self.__buscar_recursivo(atual.getEsquerda(), preco)
        else:
            return self.__buscar_recursivo(atual.getDireita(), preco)

    def buscarPorFaixaPreco(self, preco_minimo: int, preco_maximo: int):
        '''Buscar jogos por faixa de preço'''
        resultado = []
        self.__buscar_faixa(self.__raiz, preco_minimo, preco_maximo, resultado)
        return resultado

    def __buscar_faixa(self, atual: NoJogo, minimo: int, maximo: int, resultado: list[Jogo]):
        if atual is None:
            return
        if minimo <= atual.getJogo().getPreco() <= maximo:
            resultado.append(atual.getJogo())
        if minimo < atual.getJogo().getPreco():
            self.__buscar_faixa(atual.getEsquerda(), minimo, maximo, resultado)
        if atual.getJogo().getPreco() < maximo:
            self.__buscar_faixa(atual.getDireita(), minimo, maximo, resultado)
