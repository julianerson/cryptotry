from InquirerPy import inquirer

print('bem vindo ao encriptografador de ?trybulet?')

def xor():#aqui temos uma cryptografia xor, ela pode encryptografar e desincryptar
    print('\n' * 4000)
    palavra = input("diga sua palavra-chave")
    key = input("diz a chave")
    key = int(key)
    pos = "".join(chr(ord(o) ^ key)for o in palavra)#onde a magica acontece
    print(f"sua senha e {pos}")

def cesar():#cifra de cesar aqui

    command = input("vc quer cryptografar use s, ou descryptografar use f")#comando que vai dizer o que seu fulano quer

    if command == "s":#vai cryptografar em cifra de cesar
            print('\n' * 4000)#limpa a tela
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
                elif 97 <= z <= 122:#aqui a de letras
                    p = z + key
                    while 123 <= p:
                        p = p - 26
                    lo = chr(p)
                pos.append(lo)#junta tudo
            pos = "".join(pos)#transforma a lista em string
            print(
        f"""oi, bem com a chave {key} temos {pos}
obs:maiusculos sao minusculos aqui, porque?
Porque sou preguiçoso:)""") 
                       
    if command == "f":
        nkey = input("se voce sabe que uma chave nao e a certa escreva aqui, se for mais de uma voce so coloca um espaço para separar").split()
        if nkey != "":
            nkey = [int(do) for do in nkey]#diz quais chaves nao temos que usar
        
        print('\n' * 4000)
        keys = int(input("diga quantos chutes vamos dar"))#quantidade de chutes que podemos dar

        print('obs: nao pode haver virgulas, e letras maiusculas viram minusculas')

        word = input("diga sua palavra")
        word = word.lower()#por motivos de preguiça, eu nao adicionei letras maiusculas

        palavra = input("diga algo que vc ache ter na mensagem")

        for key in range(keys):#sim eu decodifico da mesma forma que codifico
            if key in nkey:
                continue
            pos = []
            for o in word:
                lo = o
                z = ord(o)#transformaçao para unicode
                if 48 <= z <= 57:
                    p = z + key
                    while p >= 58:
                        p = p - 10
                    lo = chr(p)
                elif 97 <= z <= 122:#aqui a de letras
                    p = z + key
                    while 123 <= p:
                        p = p - 26
                    lo = chr(p)
                pos.append(lo)#junta tudo
            pos = "".join(pos)#transforma a lista em string
            if palavra in pos:#diz se esta certo ou errado
                print(f'acredito que a palavra seja {pos} com a chave {key}')
                break

while True:
    print('\n' * 4000)
    cryp = inquirer.select(
        message="diga qual criptografia usar para encriptar",
        choices=["sair","xor", "cesar"],
        default="Python",
        ).execute()#aqui se encontra a GUI principal
    cryp = str(cryp)
    if "xor" in cryp:
        xor()
        continue
    elif "sair" in cryp:
        break
    elif "cesar" in cryp:
        cesar()
        continue
