intro_message = (
    "Boas vindas ao PyQuiz CC!\n"
    "Introdução à Programação em Python - P1"
)

border =  "=" * 40

print(f"{border}\n{intro_message}\n{border}")

playing = input("Gostaria de iniciar?(S/N) ").lower().strip()
valid_asnwers = ["sim", "s", "yes", "y", "true", "claro", "com certeza"]

if playing not in valid_asnwers:
    quit()

question_01 = (
    "O que é um algoritmo?\n"

    "a) É perceber semelhanças entre problemas ou situações.\n"

    "b) É uma sequência finita, lógica e bem "
    "definida de instruções, regras ou "
    "passos, para resolver um problema "
    "ou realizar uma tarefa específica.\n"

    "c) É focar no que é importante e ignorar detalhes "
    "desnecessários naquele momento.\n"

    "a, b ou c? "
)
user_answer_01 = input(question_01).lower().strip()
correct_answer_01 = "c"