borda = "=" * 40

print(borda)
print("Boas vindas ao PyQuiz CC!\nIntrodução à Programação em Python - P1")
print(borda)

jogando = input("Gostaria de iniciar?(s/n) ").lower().strip()

if jogando != "s" and jogando != "sim":
    quit()

nota = 0
opcoes_resposta = "Sua resposta(a/b/c/d): "

# ==========
# Questão 1    
# ==========
questao_01 = (
    "\n1 - O que é um algoritmo?\n"

    "a) É perceber semelhanças entre problemas ou situações.\n"

    "b) É uma sequência finita, lógica e bem "
    "definida de instruções, regras ou "
    "passos, para resolver um problema "
    "ou realizar uma tarefa específica.\n"

    "c) É focar no que é importante e ignorar detalhes "
    "desnecessários naquele momento.\n"

    "d) É um tipo de operador lógico.\n"
)
resposta_correta_01 = "b"

print(questao_01)

resposta_usuario_01 = input(opcoes_resposta).lower().strip()

if resposta_usuario_01 == resposta_correta_01:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")

# ==========
# Questão 2
# ==========
questao_02 = (
    "\n2 - Quais são os 4 pilares do pensamento computacional?\n"


    "a) Lógica, abstração, recursão e depuração.\n"


    "b) Decomposição, reconhecimento de padrões, "
    "abstração e algoritmos.\n"


    "c) Variáveis, funções, loops e condicionais.\n"


    "d) Entrada, processamento, saída e armazenamento.\n"
)
resposta_correta_02 = "b"


print(questao_02)


resposta_usuario_02 = input(opcoes_resposta).lower().strip()


if resposta_usuario_02 == resposta_correta_02:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 3
# ==========
questao_03 = (
    "\n3 - O que é uma variável?\n"


    "a) É um comando que exibe informações na tela.\n"


    "b) É uma sequência de instruções para resolver um problema.\n"


    "c) É um espaço na memória usado para armazenar um valor "
    "que pode ser utilizado depois no programa.\n"


    "d) É um tipo de estrutura de repetição.\n"
)
resposta_correta_03 = "c"


print(questao_03)


resposta_usuario_03 = input(opcoes_resposta).lower().strip()


if resposta_usuario_03 == resposta_correta_03:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 4
# ==========
questao_04 = (
    "\n4 - Analise as afirmativas abaixo e assinale a opção correta:\n"
    "I.   Uma variável pode começar com letra e '_'.\n"
    "II.  Uma variável pode começar com número.\n"
    "III. Uma variável pode conter letras, números e '_'.\n"
    "IV.  Uma variável pode conter espaços.\n"
    "V.   Uma variável pode conter caracteres especiais como @, #, %.\n\n"


    "a) Apenas I e II são verdadeiras.\n"


    "b) Apenas II, IV e V são verdadeiras.\n"


    "c) Apenas I e III são verdadeiras.\n"


    "d) Todas as afirmativas são verdadeiras.\n"
)
resposta_correta_04 = "c"


print(questao_04)


resposta_usuario_04 = input(opcoes_resposta).lower().strip()


if resposta_usuario_04 == resposta_correta_04:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 5
# ==========
questao_05 = (
    "\n5 - Qual das declarações de variáveis abaixo está INCORRETA?\n\n"
    "a) nome = 'Gabriel'\n"
    "b) _var = 13.5\n"
    "c) cliente_1 = 'user'\n"
    "d) class = 'p1'\n"
)
resposta_correta_05 = "d"


print(questao_05)


resposta_usuario_05 = input(opcoes_resposta).lower().strip()


if resposta_usuario_05 == resposta_correta_05:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 6
# ==========
questao_06 = (
    "\n6 - O que o símbolo de igual (=) representa na declaração "
    "de uma variável em Python?\n"


    "a) Comparação entre dois valores.\n"


    "b) Atribuição de um valor à variável.\n"


    "c) Um operador matemático de soma.\n"


    "d) Indica o fim de uma linha de código.\n"
)
resposta_correta_06 = "b"


print(questao_06)


resposta_usuario_06 = input(opcoes_resposta).lower().strip()


if resposta_usuario_06 == resposta_correta_06:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 7
# ==========
questao_07 = (
    "\n7 - Quais são os principais tipos básicos de dados em Python?\n"


    "a) INT, CHAR, DOUBLE e BOOLEAN.\n"


    "b) NUMBER, TEXT, LOGIC e ARRAY.\n"


    "c) INT, FLOAT, STR e BOOL.\n"


    "d) INT, FLOAT, CHAR e NULL.\n"
)
resposta_correta_07 = "c"


print(questao_07)


resposta_usuario_07 = input(opcoes_resposta).lower().strip()


if resposta_usuario_07 == resposta_correta_07:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 8
# ==========
questao_08 = (
    "\n8 - Qual das variáveis abaixo é do tipo STRING (str)?\n\n"
    "a) idade = 21\n"
    "b) altura = 1.75\n"
    "c) nome = 'Gabriel'\n"
    "d) aprovado = True\n"
)
resposta_correta_08 = "c"


print(questao_08)


resposta_usuario_08 = input(opcoes_resposta).lower().strip()


if resposta_usuario_08 == resposta_correta_08:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 9
# ==========
questao_09 = (
    "\n9 - Qual das variáveis abaixo é do tipo FLOAT?\n\n"
    "a) ano = 2026\n"
    "b) media = 7.5\n"
    "c) curso = 'CC'\n"
    "d) passou = False\n"
)
resposta_correta_09 = "b"


print(questao_09)


resposta_usuario_09 = input(opcoes_resposta).lower().strip()


if resposta_usuario_09 == resposta_correta_09:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 10
# ==========
questao_10 = (
    "\n10 - O que a função input() faz no Python?\n"


    "a) Exibe uma mensagem na tela para o usuário.\n"


    "b) Realiza cálculos matemáticos automaticamente.\n"


    "c) Lê um valor digitado pelo usuário e "
    "o retorna como texto.\n"


    "d) Encerra a execução do programa.\n"
)
resposta_correta_10 = "c"


print(questao_10)


resposta_usuario_10 = input(opcoes_resposta).lower().strip()


if resposta_usuario_10 == resposta_correta_10:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 11
# ==========
questao_11 = (
    "\n11 - O que a função print() faz no Python?\n"


    "a) Lê um valor digitado pelo usuário.\n"


    "b) Exibe uma mensagem ou valor na tela.\n"


    "c) Armazena um valor na memória.\n"


    "d) Verifica se uma condição é verdadeira ou falsa.\n"
)
resposta_correta_11 = "b"


print(questao_11)


resposta_usuario_11 = input(opcoes_resposta).lower().strip()


if resposta_usuario_11 == resposta_correta_11:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 12
# ==========
questao_12 = (
    "\n12 - Quais operadores aritméticos representam as quatro "
    "operações básicas da matemática no Python?\n"


    "a) +, -, *, /\n"


    "b) +, -, x, ÷\n"


    "c) soma(), sub(), mult(), div()\n"


    "d) +, -, **, %\n"
)
resposta_correta_12 = "a"


print(questao_12)


resposta_usuario_12 = input(opcoes_resposta).lower().strip()


if resposta_usuario_12 == resposta_correta_12:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 13
# ==========
questao_13 = (
    "\n13 - O que o operador '//' faz no Python?\n"


    "a) Divide dois números e retorna o resultado com decimais.\n"


    "b) Calcula o resto da divisão entre dois números.\n"


    "c) Divide dois números e retorna apenas "
    "a parte inteira do resultado.\n"


    "d) É utilizado para escrever comentários no código.\n"
)
resposta_correta_13 = "c"


print(questao_13)


resposta_usuario_13 = input(opcoes_resposta).lower().strip()


if resposta_usuario_13 == resposta_correta_13:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 14
# ==========
questao_14 = (
    "\n14 - Como se encontra o resto de uma divisão no Python?\n"


    "a) Usando o operador //\n"


    "b) Usando o operador %\n"


    "c) Usando o operador **\n"


    "d) Usando a função resto()\n"
)
resposta_correta_14 = "b"


print(questao_14)


resposta_usuario_14 = input(opcoes_resposta).lower().strip()


if resposta_usuario_14 == resposta_correta_14:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 15
# ==========
questao_15 = (
    "\n15 - Como se calcula uma potência no Python?\n\n"
    "a) 2 ^ 3\n"
    "b) 2 ** 3\n"
    "c) pot(2, 3)\n"
    "d) 2 * 3\n"
)
resposta_correta_15 = "b"


print(questao_15)


resposta_usuario_15 = input(opcoes_resposta).lower().strip()


if resposta_usuario_15 == resposta_correta_15:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 16
# ==========
questao_16 = (
    "\n16 - Como o Python é interpretado pelo computador?\n"


    "a) Todo o código é compilado de uma vez antes de executar.\n"


    "b) O código é lido e executado linha por linha, "
    "de cima para baixo.\n"


    "c) O código é convertido para binário e depois executado.\n"


    "d) O Python só executa o código se não houver erros "
    "em nenhuma linha.\n"
)
resposta_correta_16 = "b"


print(questao_16)


resposta_usuario_16 = input(opcoes_resposta).lower().strip()


if resposta_usuario_16 == resposta_correta_16:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 17
# ==========
questao_17 = (
    "\n17 - O que é uma estrutura de decisão na programação?\n"


    "a) É uma estrutura que repete um bloco de código "
    "várias vezes.\n"


    "b) É uma estrutura que permite ao programa escolher "
    "qual caminho seguir com base em uma condição.\n"


    "c) É uma estrutura usada para armazenar "
    "vários valores ao mesmo tempo.\n"


    "d) É uma função que recebe dados do usuário.\n"
)
resposta_correta_17 = "b"


print(questao_17)


resposta_usuario_17 = input(opcoes_resposta).lower().strip()


if resposta_usuario_17 == resposta_correta_17:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 18
# ==========
questao_18 = (
    "\n18 - Analise o código abaixo:\n\n"
    "   nota = float(input('Digite sua nota: '))\n\n"
    "   if nota >= 7:\n"
    "       print('Aprovado')\n"
    "   elif nota >= 5:\n"
    "       print('Recuperação')\n"
    "   else:\n"
    "       print('Reprovado')\n\n"
    "Qual estrutura é utilizada para tratar mais de "
    "duas condições diferentes no código acima?\n"


    "a) Apenas if e else.\n"


    "b) if, elif e else — onde elif verifica uma condição "
    "adicional entre o if e o else.\n"


    "c) Somente elif.\n"


    "d) O código está incorreto e não funciona.\n"
)
resposta_correta_18 = "b"


print(questao_18)


resposta_usuario_18 = input(opcoes_resposta).lower().strip()


if resposta_usuario_18 == resposta_correta_18:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 19
# ==========
questao_19 = (
    "\n19 - Qual operador relacional deve ser usado para verificar "
    "se dois valores são DIFERENTES em Python?\n"


    "a) ==\n"


    "b) >=\n"


    "c) !=\n"


    "d) =\n"
)
resposta_correta_19 = "c"


print(questao_19)


resposta_usuario_19 = input(opcoes_resposta).lower().strip()


if resposta_usuario_19 == resposta_correta_19:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")


# ==========
# Questão 20
# ==========
questao_20 = (
    "\n20 - Analise o código abaixo:\n\n"
    "   # O usuário digitou: 16\n"
    "   idade = int(input('Digite sua idade: '))\n\n"
    "   if idade >= 18:\n"
    "       print('Maior de idade')\n"
    "   else:\n"
    "       print('Menor de idade')\n\n"
    "Qual será a saída exibida na tela?\n"


    "a) Maior de idade\n"


    "b) Menor de idade\n"


    "c) O código apresentará um erro.\n"


    "d) Nada será exibido na tela.\n"
)
resposta_correta_20 = "b"


print(questao_20)


resposta_usuario_20 = input(opcoes_resposta).lower().strip()


if resposta_usuario_20 == resposta_correta_20:
    print("Correto!")
    nota += 1
else:
    print("Incorreto!")

# =================
# Resultados finais
# =================

nota_porcentagem = round((nota / 20) * 100)

print(borda)
print("Resultado final:")
print("Você acertou", nota, "de 20 questões!")
print("Aproveitamento:", str(nota_porcentagem) + "%")
print(borda)