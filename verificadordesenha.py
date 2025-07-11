import re

# Lista para armazenar senhas fortes
senhas_fortes = []

# Função para validar a senha
def senha_e_forte(senha):
    tem_8_caracteres = len(senha) >= 8
    tem_maiuscula = re.search(r"[A-Z]", senha)
    tem_numero = re.search(r"[0-9]", senha)
    tem_simbolo = re.search(r"[!@#$%^&*()\-_=+{}[\]:;,.<>?/\\|]", senha)

    if tem_8_caracteres and tem_maiuscula and tem_numero and tem_simbolo:
        return True
    else:
        print("❌ Senha fraca. Ela deve conter:")
        if not tem_8_caracteres:
            print("- Pelo menos 8 caracteres")
        if not tem_maiuscula:
            print("- Pelo menos 1 letra maiúscula")
        if not tem_numero:
            print("- Pelo menos 1 número")
        if not tem_simbolo:
            print("- Pelo menos 1 símbolo (ex: !, @, #, etc)")
        return False

# Loop até a senha ser forte
while True:
    senha = input("Digite uma senha forte: ")
    if senha_e_forte(senha):
        senhas_fortes.append(senha)
        print("✅ Senha forte salva com sucesso!")
        break  # remove o break se quiser aceitar várias senhas seguidas

# Exibe a lista de senhas fortes
print("\nSenhas fortes salvas:")
for i, s in enumerate(senhas_fortes, start=1):
    print(f"{i}. {s}")

