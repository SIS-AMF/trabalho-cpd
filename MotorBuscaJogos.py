from ArvoreJogos import ArvoreJogos
from HashGeneros import HashGeneros
from Jogo import Jogo


class MotorBuscaJogos:
    """Motor de busca que combina árvores e hash tables para manipular jogos."""

    __catalogo_jogos: ArvoreJogos
    __generos: HashGeneros

    def __init__(self):
        self.__catalogo_jogos = ArvoreJogos()
        self.__generos = HashGeneros(10)

    def adicionarJogo(self, jogo: Jogo) -> None:
        self.__catalogo_jogos.inserir(jogo)
        self.__generos.adicionarJogoHash(jogo)

    def buscarPorPreco(self, preco: float) -> list[Jogo]:
        return self.__catalogo_jogos.buscarPorPreco(preco)

    def buscarPorFaixaPreco(self, minimo: float, maximo: float) -> list[Jogo]:
        return self.__catalogo_jogos.buscarPorFaixaPreco(minimo, maximo)

    def buscarPorGenero(self, genero: str) -> list[Jogo]:
        return self.__generos.obterJogosHash(genero)
    
    def getCatalogoEmOrdem(self):
        return self.__catalogo_jogos.preOrder()
