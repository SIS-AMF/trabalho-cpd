class Jogo:
    """Representa um jogo no sistema."""

    __id: int
    __nome: str
    __desenvolvedora: str
    __preco: float
    __generos: list[str]

    def __init__(self, id: int, nome: str, desenvolvedora: str, preco: float, generos: list[str]) -> None:
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if not generos:
            raise ValueError("O jogo deve ter pelo menos um gênero.")
        self.__id = id
        self.__nome = nome
        self.__desenvolvedora = desenvolvedora
        self.__preco = preco
        self.__generos = generos

    # Getters
    def getId(self) -> int:
        return self.__id

    def getNome(self) -> str:
        return self.__nome

    def getDesenvolvedora(self) -> str:
        return self.__desenvolvedora

    def getPreco(self) -> float:
        return self.__preco

    def getGeneros(self) -> list[str]:
        return self.__generos

    # Setters
    def setPreco(self, preco: float) -> None:
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = preco

    def setGeneros(self, generos: list[str]) -> None:
        if not generos:
            raise ValueError("O jogo deve ter pelo menos um gênero.")
        self.__generos = generos

    def __repr__(self) -> str:
        return (
            f"Jogo(ID: {self.__id}, "
            f"Título: '{self.__nome}', "
            f"Desenvolvedora: {self.__desenvolvedora}, "
            f"Preço: R${self.__preco:.2f}, "
            f"Gêneros: {self.__generos})"
        )
