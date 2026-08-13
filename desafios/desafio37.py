
import random

print("| GACCHA PY-LOKO |")

premios = ["Papel A4","Liquidificador","Ovo Mexido","Coxinha","Controle Remoto","T-Rex","Ovo Normal","iPhone Pro Max 19 HD 4K 60fps 80gb de RAM 50tb de Armazenamento Camera 1px","Papelão"]

for i in range (1,4):
    premio = random.choice(premios)
    print(f"{i}º Tentativa: {premio}")

    if premio == "Papelão":
        print("VOCÊ CONSEGUIU O MAIOR PRÊMIO DE TODOS!")
        break
    elif i == 3:
        print("Você não conseguiu o melhor prêmio e agora ficou sem nada!")
    else:
        print("Aperte enter para uma nova tentativa ou digite 'parar' para manter o prêmio...")
        escolha = input("")
        if escolha == "parar":
            print(f"Você manteve o prêmio {premio}!")
            break