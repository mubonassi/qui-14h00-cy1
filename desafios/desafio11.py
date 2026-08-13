print("| Adivinhar Senha |")
senha = "abc123"
tentativa = input("Digite a sua tentativa de senha: ")

if tentativa == senha:
    print("Você acertou a senha!")
else:
    print(f"Você ERROU a senha! A senha era {senha}")