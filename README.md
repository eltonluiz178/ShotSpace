# 🚀 ShotSpace

ShotSpace é um jogo de nave espacial desenvolvido com Python e Pygame,
onde asteroides e inimigos surgem verticalmente na tela e o objetivo é
sobreviver e destruí-los através de disparos.

Este projeto faz parte da minha jornada no desenvolvimento de jogos,
onde explorei conceitos como movimentação, detecção de colisões,
efeitos sonoros, sistema de power-ups e organização de código com Pygame.

---

## 🎮 Como Jogar

- **Mover:** Setas do teclado ou WASD  
- **Atirar:** Espaço  
- **Objetivo:** Sobreviva o maior tempo possível destruindo tudo que aparecer!

---

## ✨ Funcionalidades

- 🌑 Asteroides e inimigos surgindo progressivamente na tela
- 🔫 Sistema de disparos
- ⚡ Sistema de power-ups com 2 tipos:
  - ❤️ **Vida extra** — recupere sua saúde
  - 🔫 **Multi-disparo** — atire mais projéteis simultaneamente
- 🎲 Power-ups surgem aleatoriamente ou dropam de inimigos e asteroides destruídos
- 🔊 Efeitos sonoros

---

## 📦 Como Executar

### Pelo executável (recomendado)
Baixe o executável na seção [Releases](../../releases) e execute diretamente.  
Não requer instalação.

### Pelo código-fonte

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/ShotSpace.git
cd ShotSpace
```

**2. Instale as dependências**
```bash
pip install pygame
```

**3. Execute o jogo**
```bash
python src/main.py
```

---

## 🛠️ Gerando o Executável

Para gerar o executável do jogo localmente, rode:

```bash
pyinstaller --onefile --noconsole --add-data "assets;assets" --name ShotSpace --icon=assets/images/gameIcon.ico src/main.py
```

O arquivo gerado estará na pasta `dist/`.

---

## 🔮 Roadmap

- [ ] Sistema de disparo para os inimigos
- [ ] Sistema de waves progressivas
- [ ] Boss fights
- [ ] Launcher com menu de configurações
- [ ] Melhorias visuais e novas mecânicas

---

## 🐛 Bugs & Sugestões

Encontrou um bug ou tem uma sugestão?  
Abra uma [issue](../../issues) que terei prazer em analisar!

---

## 🧰 Tecnologias

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
- [PyInstaller](https://pyinstaller.org/)
