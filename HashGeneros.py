from Jogo import Jogo


class HashGeneros:
    """Hash table para organizar jogos por gênero."""
    __table: dict[str, list[Jogo]]
    __table2: dict[str, list[Jogo]]
    __tamanho: int

    def __init__(self, tamanho: int):
        self.__table = {}
        self.__tamanho = tamanho
        self.__table2 = {i: [] for i in range(tamanho)}

    def hash(self, valor: str):
        total = 0
        for x in valor:
            total += ord(x)
        return total % self.__tamanho

    def adicionarJogoHash(self, jogo: Jogo) -> None:
        for genero in jogo.getGeneros():
            hash = self.hash(genero)
            if hash not in self.__table2:
                self.__table2[hash] = []
            self.__table2[hash].append(jogo)

    def obterJogosHash(self, genero: str) -> list[Jogo]:
        hash = self.hash(genero)
        return self.__table2.get(hash, [])

    def adicionarJogo(self, jogo: Jogo) -> None:
        for genero in jogo.getGeneros():
            if genero not in self.__table:
                self.__table[genero] = []
            self.__table[genero].append(jogo)

    def obterJogos(self, genero: str) -> list[Jogo]:
        return self.__table.get(genero, [])
