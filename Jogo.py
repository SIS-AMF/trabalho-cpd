class Jogo:
    """Objeto que armazena um jogo."""

    __id: int
    __nome: str
    __desenvolvedora: str
    __preco: float
    __generos: list[str]

    def __init__(
        self, id: int, nome: str, desenvolvedora: str, preco: float, generos: list[str]
    ) -> None:
        self.__id = id
        self.__nome = nome
        self.__desenvolvedora = desenvolvedora
        self.__preco = preco
        self.__generos = generos

    # Getters

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getDesenvolvedora(self):
        return self.__desenvolvedora

    def getPreco(self):
        return self.__preco

    def getGeneros(self):
        return self.__generos

    # Setters

    def setPreco(self, preco: int):
        self.__preco = preco

    def setGeneros(self, generos: list[str]):
        self.__generos = generos

    def __repr__(self) -> str:
        return f"Jogo(ID: {self.__id}, Título: {self.__nome}, Preço: {self.__preco}, Gêneros: {self.__generos})"
