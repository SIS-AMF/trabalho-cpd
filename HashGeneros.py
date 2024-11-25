from Jogo import Jogo


class HashGeneros:
    __genero_para_jogos: dict

    def __init__(self):
        self.__genero_para_jogos = {}

    def adicionarJogo(self, jogo: Jogo):
        '''Adicionar um jogo ao hash table'''
        for genero in jogo.getGeneros():
            if genero not in self.__genero_para_jogos:
                self.__genero_para_jogos[genero] = []
            self.__genero_para_jogos[genero].append(jogo)

    def obterJogos(self, genero: str):
        '''Buscar jogos por gênero'''
        return self.__genero_para_jogos.get(genero, [])
