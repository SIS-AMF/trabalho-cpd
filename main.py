from Jogo import Jogo
from MotorBuscaJogos import MotorBuscaJogos

if __name__ == "__main__":
    loja = MotorBuscaJogos()

    # Adicionando jogos fictícios
    jogo1 = Jogo(1, "Minecraft", "Mojang", 100, ["Ação", "Mundo Aberto"])
    jogo2 = Jogo(2, "The Witcher 3", "CD Projekt", 150, ["RPG", "Ação"])
    jogo3 = Jogo(3, "Stardew Valley", "ConcernedApe", 50, ["Simulação", "Indie"])
    jogo4 = Jogo(4, "Celeste", "Maddy Makes Games", 75, ["Plataforma", "Indie"])
    jogo5 = Jogo(5, "Hollow Knight", "Team Cherry", 75, ["Metroidvania", "Indie"])

    loja.adicionarJogo(jogo1)
    loja.adicionarJogo(jogo2)
    loja.adicionarJogo(jogo3)
    loja.adicionarJogo(jogo4)
    loja.adicionarJogo(jogo5)

    # Buscas
    print("Jogos com preço exato de 75:")
    print(loja.buscarPorPreco(75))

    print("\nJogos com preço entre 50 e 100:")
    print(loja.buscarPorFaixaPreco(50, 100))

    print("\nJogos do gênero 'Indie':")
    print(loja.buscarPorGenero("Indie"))

    print("\nJogos do gênero 'RPG':")
    print(loja.buscarPorGenero("RPG"))
