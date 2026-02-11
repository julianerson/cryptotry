from InquirerPy import inquirer

print('bem vindo ao encriptografador de ?trybulet?')

def xor():#aqui temos uma cryptografia xor, ela pode encryptografar e desincryptar
    palavra = input("diga sua palavra-chave")
    key = input("diz a chave")
    key = int(key)
    pos = "".join(chr(ord(o) ^ key)for o in palavra)#onde a magica acontece
    print(f"sua senha e {pos}")
def cesar():#cifra de cesar aqui
    pos = []#parte nescessaria para a identaçao
    print('obs: nao pode haver virgulas, e letras maiusculas viram minusculas')
    word = input("diga sua palavra")
    word = word.lower()#por motivos de preguiça, eu nao adicionei letras maiusculas
    key = int(input("diga a chave"))#chave para decodificar
    for o in word:
        lo = o
        z = ord(o)#transformaçao para unicode
        if 48 <= z <= 57:
            p = z + key
            while p >= 58:
                p = p - 10
            lo = chr(p)
        if 97 <= z <= 122:#aqui a de letras
            p = z + key
            while 123 <= p:
                p = p - 26
            lo = chr(p)
        pos.append(lo)#junta tudo
    pos = "".join(pos)#transforma a lista em string
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
