intro_message = (
    "Boas vindas ao PyQuiz CC!\n"
    "Introdução à Programação em Python - P1"
)

border =  "=" * 40

print(f"{border}\n{intro_message}\n{border}")

playing = input("Gostaria de iniciar?(s/n) ").lower().strip()
valid_asnwers = ["sim", "s", "yes", "y", "true", "claro", "com certeza"]

if playing not in valid_asnwers:
    quit()

answer_options = "Sua resposta(a/b/c/d): "

question_01 = (
    "O que é um algoritmo?\n"

    "a) É perceber semelhanças entre problemas ou situações.\n"

    "b) É uma sequência finita, lógica e bem "
    "definida de instruções, regras ou "
    "passos, para resolver um problema "
    "ou realizar uma tarefa específica.\n"

    "c) É focar no que é importante e ignorar detalhes "
    "desnecessários naquele momento.\n"

    "d) É um tipo de operador lógico."
)
correct_answer_01 = "b"
user_answer_01 = input(f"{question_01}\n{answer_options}").lower().strip()