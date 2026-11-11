# Apresentação do Projeto - Jogo da Forca

## 1. Problema

O objetivo do projeto foi desenvolver um Jogo da Forca em Python.

O programa deve escolher uma palavra e permitir que o jogador tente descobri-la digitando uma letra de cada vez.

O jogador tem no máximo 6 tentativas erradas. O programa deve validar as letras introduzidas, mostrar as letras corretas nas suas posições e informar no final se o jogador venceu ou perdeu.

## 2. Demonstração do jogo

Para iniciar o jogo, executar no terminal:

python main.py

Exemplo:

=== JOGO DA FORCA ===

Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: p

Você acertou!

Palavra: p _ _ _ _ _
Tentativas restantes: 6

O jogo continua até o jogador descobrir toda a palavra ou atingir o limite de 6 tentativas erradas.

## 3. Decisões técnicas

O projeto foi desenvolvido em Python e dividido nos ficheiros main.py e jogo.py para manter o código organizado.

Foi utilizada a biblioteca random para escolher uma palavra aleatoriamente.

Foram criadas funções para separar as diferentes tarefas do jogo, como escolher a palavra, mostrar as letras descobertas e controlar o jogo.

Também foram implementadas validações para impedir números, caracteres especiais, mais de uma letra e letras já utilizadas.

Foi utilizado try/except para tratar possíveis erros durante a entrada do jogador.

Foram realizados 5 testes válidos e 5 testes inválidos para verificar o funcionamento do programa em diferentes situações.

## 4. Melhorias futuras

Como melhorias futuras, o Jogo da Forca poderá receber novas funcionalidades, como:

- Criar diferentes níveis de dificuldade.
- Adicionar categorias de palavras.
- Criar um sistema de pontuação.
- Mostrar o desenho da forca a cada tentativa errada.
- Desenvolver uma interface gráfica para tornar o jogo mais interativo.
- Permitir que o jogador escolha jogar novamente sem reiniciar o programa.

