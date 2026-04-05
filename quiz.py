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

print("testado!")