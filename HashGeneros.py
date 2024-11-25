from Jogo import Jogo


class HashGeneros:
    """Hash table para organizar jogos por gênero."""

    __genero_para_jogos: dict[str, list[Jogo]]

    def __init__(self):
        self.__genero_para_jogos = {}

    def adicionarJogo(self, jogo: Jogo) -> None:
        for genero in jogo.getGeneros():
            if genero not in self.__genero_para_jogos:
                self.__genero_para_jogos[genero] = []
            self.__genero_para_jogos[genero].append(jogo)

    def obterJogos(self, genero: str) -> list[Jogo]:
        return self.__genero_para_jogos.get(genero, [])
