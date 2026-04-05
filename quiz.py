borda = "=" * 40

print(borda)
print("Boas vindas ao PyQuiz CC!\nIntrodução à Programação em Python - P1")
print(borda)

jogando = input("Gostaria de iniciar?(s/n) ").lower().strip()

if jogando != "s" and jogando != "sim":
    quit()

opcoes_de_resposta = "Sua resposta(a/b/c/d): "

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
resposta_01 = "b"

print(questao_01)

user_answer_01 = input(opcoes_de_resposta).lower().strip()
