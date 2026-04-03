# ShotSpace
Este projeto faz parte do meu aprendizado em desenvolvimento de jogos, onde explorei conceitos básicos como movimentação da nave, detecção de colisões e implementação de efeitos sonoros. Também foi uma oportunidade para praticar organização de código e entender melhor como estruturar um jogo utilizando a biblioteca Pygame.

## Criando o executável do game

Rode o seguinte comando para criar o executável do jogo :
```bash
pyinstaller --onefile --noconsole --add-data "assets;assets" --name ShotSpace --icon=assets/images/gameIcon.ico src/main.py
```
