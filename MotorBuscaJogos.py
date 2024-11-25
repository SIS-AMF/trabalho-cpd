from ArvoreJogos import ArvoreJogos
from HashGeneros import HashGeneros
from Jogo import Jogo


class MotorBuscaJogos:
    __catalogo_jogos: ArvoreJogos
    __generos: HashGeneros

    def __init__(self):
        self.__catalogo_jogos = ArvoreJogos()
        self.__generos = HashGeneros()

    def adicionarJogo(self, jogo: Jogo):
        self.__catalogo_jogos.inserir(jogo)
        self.__generos.adicionarJogo(jogo)

    def buscarPorPreco(self, preco: int):
        return self.__catalogo_jogos.buscarPorPreco(preco)

    def buscarPorFaixaPreco(self, minimo: int, maximo: int):
        return self.__catalogo_jogos.buscarPorFaixaPreco(minimo, maximo)

    def buscarPorGenero(self, genero: str):
        return self.__generos.obterJogos(genero)
