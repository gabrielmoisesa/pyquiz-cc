# PyQuiz CC 🐍

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Nível: Iniciante](https://img.shields.io/badge/Nível-Iniciante-green?style=flat-square)](#sobre-o-projeto)

Um quiz interativo de terminal sobre os conteúdos de Introdução à Programação em Python.

<details>
  <summary>Índice</summary>

1. [Sobre o Projeto](#sobre-o-projeto)
   - [Conteúdos Abordados](#conteúdos-abordados)
   - [Feito Com](#feito-com)
2. [Como Executar](#como-executar)
   - [Pré-requisitos](#pré-requisitos)
   - [Instalação e Execução](#instalação-e-execução)
3. [Créditos](#créditos)
4. [Licença](#licença)

</details>

## Sobre o Projeto

PyQuiz CC é um quiz de terminal com 20 questões de múltipla escolha sobre os conteúdos iniciais
de Introdução à Programação em Python, desenvolvido para a turma de Ciência da Computação da UNIESP.

O código foi escrito utilizando apenas os conceitos básicos aprendidos em aula:
variáveis, tipos de dados, `input()`, `print()`, operadores e estruturas de decisão (`if/else`)
e conta com comentários didáticos ao longo do código para facilitar o entendimento.

> Desenvolvido por **Gabriel Moises Alves** - Ciência da Computação, UNIESP.

### Conteúdos Abordados

- Algoritmos e pensamento computacional
- Variáveis: declaração, tipos e regras de nomenclatura
- Tipos de dados: `int`, `float`, `str`, `bool`
- Funções `input()` e `print()`
- Operadores aritméticos (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Operadores relacionais (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Estruturas de decisão: `if`, `elif`, `else`

### Feito Com

- Python 3

## Como Executar

### Pré-requisitos

**1. Python 3**

Você precisará ter o [Python 3](https://www.python.org/downloads/) instalado na máquina.
Acesse o link, baixe o instalador para Windows e siga os passos.

> ⚠️ Durante a instalação, marque a opção **"Add Python to PATH"** antes de clicar em Install.
> Sem isso, o Python pode não ser reconhecido no terminal.

Para verificar se a instalação foi concluída com sucesso, abra o terminal e execute:

```bash
python --version
```

Se aparecer algo como `Python 3.x.x`, está tudo certo! ✅

---

**2. VS Code (opcional, mas recomendado)**

Se for rodar o projeto pelo [Visual Studio Code](https://code.visualstudio.com/), instale a extensão
oficial do Python para ter suporte a syntax highlight, execução direta e detecção de erros:

🔗 [Python — Extensão para VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Ou pesquise por **"Python"** na aba de extensões do VS Code (`Ctrl + Shift + X`) e instale
a extensão da **Microsoft**.

### Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/gabrielmoisesa/pyquiz-cc.git
   ```

   Ou baixe o projeto como `.zip` clicando em **Code → Download ZIP** no GitHub e extraia a pasta.

2. Navegue até a pasta do projeto:

   ```bash
   cd pyquiz-cc
   ```

3. Execute o quiz:
   ```bash
   python quiz.py
   ```

> 💡 Se estiver no VS Code, você também pode abrir o arquivo `quiz.py` e clicar no botão
> **▶ Run Python File** no canto superior direito da tela.

## Créditos

- Inspirado no projeto [Quiz Game](https://github.com/techwithtim/5-Python-Projects-For-Beginners/blob/main/quiz_game.py)
  de [Tim Ruscica (Tech With Tim)](https://github.com/techwithtim)

## Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](LICENSE) para mais informações.
