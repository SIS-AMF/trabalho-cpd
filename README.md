# Sistema de Gerenciamento de Jogos

Este projeto é um sistema de gerenciamento e busca de jogos que utiliza estruturas de dados como árvores binárias de busca e tabelas hash para organizar e filtrar jogos por preço e gênero.

## Estrutura do Projeto

- **ArvoreJogos.py**: Implementa uma árvore binária de busca para armazenar e consultar jogos com base no preço.
- **HashGeneros.py**: Utiliza uma tabela hash para organizar os jogos por gêneros.
- **Jogo.py**: Classe que representa um jogo no sistema, contendo atributos como ID, nome, desenvolvedora, preço e gêneros.
- **NoJogo.py**: Representa os nós da árvore binária de jogos.
- **MotorBuscaJogos.py**: Combina a funcionalidade da árvore binária e da tabela hash para gerenciar jogos de forma eficiente.
- **main.py**: Script principal que demonstra a funcionalidade do sistema.

## Funcionalidades

### Adicionar Jogos
Os jogos podem ser adicionados ao sistema usando a classe `MotorBuscaJogos`. Eles são armazenados simultaneamente na árvore binária e na tabela hash.

### Busca por Preço
- **Preço Exato**: Busca jogos com um preço específico.
- **Faixa de Preço**: Retorna jogos dentro de uma faixa de preço.

### Busca por Gênero
Busca jogos associados a um gênero específico.

### Exibição Ordenada
Retorna o catálogo completo de jogos em ordem crescente de preço.

## Exemplo de Uso

```python
from Jogo import Jogo
from MotorBuscaJogos import MotorBuscaJogos

loja = MotorBuscaJogos()

jogo1 = Jogo(1, "Minecraft", "Mojang", 100, ["Ação", "Mundo Aberto"])
jogo2 = Jogo(2, "The Witcher 3", "CD Projekt", 150, ["RPG", "Ação"])
loja.adicionarJogo(jogo1)
loja.adicionarJogo(jogo2)

# Busca por preço
print(loja.buscarPorPreco(100))

# Busca por faixa de preço
print(loja.buscarPorFaixaPreco(50, 150))

# Busca por gênero
print(loja.buscarPorGenero("Ação"))
```

## Requisitos

- Python 3.8 ou superior.

## Como Executar

1. Clone o repositório.
2. Instale as dependências (se necessário).
3. Execute o arquivo `main.py`:

```bash
python main.py
```