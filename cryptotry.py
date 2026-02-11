from InquirerPy import inquirer

print('bem vindo ao encriptografador de ?trybulet?')

def xor():
    palavra = input("diga sua palavra-chave")
    key = input("diz a chave")
    key = int(key)
    pos = "".join(chr(ord(o) ^ key)for o in palavra)
    print(f"sua senha e {pos}")
def cesar():
    pos = []
    print('obs: nao pode haver virgulas, e letras maiusculas viram minusculas')
    word = input("diga sua palavra")
    word = word.lower()
    key = int(input("diga a chave"))
    for o in word:
        z = ord(o)
        if 48 <= z <= 57:
            p = z + key
            if 58 <= p:
                p = p - 10
            lo = chr(p)
        if 97 <= z <= 122:
            p = z + key
            if 123 <= p:
                p = p - 26
            lo = chr(p)
        else:
            lo = o
        pos.append(lo)
    pos = "".join(pos)
    print(
        f"""oi, bem com a chave {key} temos {pos}
obs:maiusculos sao minusculos aqui, porque?
Porque sou preguiçoso:)"""
)

while True:
    cryp = inquirer.select(
        message="diga qual criptografia usar para encriptar",
        choices=["sair","xor", "cesar"],
        default="Python",
        ).execute()
    cryp = str(cryp)
    if "xor" in cryp:
        xor()
        continue
    elif "sair" in cryp:
        break
    elif "cesar" in cryp:
        cesar()
        continue
