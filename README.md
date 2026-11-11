# Jogo da Forca

## Objetivo do jogo

O objetivo do Jogo da Forca é descobrir uma palavra escondida.
O jogador deverá tentar descobrir a palavra escolhendo uma letra de cada vez, antes de atingir o número máximo de tentativas erradas.

## Regras principais

- O programa escolhe uma palavra escondida.
- O jogador digita uma letra de cada vez.
- Se a letra existir na palavra, ela será mostrada na posição correta.
- Se a letra não existir, será considerada uma tentativa errada.

## Condições de vitória e derrota

O jogador vence quando conseguir descobrir todas as letras da palavra.

O jogador perde quando atingir o número máximo de tentativas erradas sem descobrir a palavra.

## Limitações

- O jogador terá no máximo 6 tentativas erradas.
- Só será permitido digitar uma letra de cada vez.
- Números e outros caracteres não serão aceitos.

## Requisitos Funcionais

1. O sistema deve escolher uma palavra para o jogador tentar adivinhar.
2. O sistema deve permitir que o jogador digite uma letra de cada vez.
3. O sistema deve verificar se a letra digitada existe na palavra.
4. O sistema deve mostrar as letras corretas nas suas posições.
5. O sistema deve contabilizar as tentativas erradas do jogador.
6. O sistema deve informar se o jogador venceu ou perdeu.

## Requisitos Não Funcionais

1. O jogo deve ser simples e fácil de utilizar.
2. O sistema deve aceitar apenas letras como entrada.
3. O jogo deve apresentar as informações de forma clara para o jogador.

## Instruções de execução

1. Ter o Python instalado no computador.
2. Abrir a pasta do projeto no Visual Studio Code.
3. Abrir o terminal.
4. Executar o comando:

python main.py

5. O Jogo da Forca será iniciado no terminal.

## Exemplo de utilização

Ao executar o programa, será apresentado:

=== JOGO DA FORCA ===

Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: p

Se a letra existir na palavra:

Você acertou!

Se a letra não existir:

Você errou!

O jogo termina quando o jogador descobrir a palavra ou atingir o limite de 6 tentativas erradas.