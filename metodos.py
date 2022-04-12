def corrigirMetodo1(gabarito, resposta, nAlternativas):
    gabarito = int(gabarito)
    resposta = int(resposta)
    if not validar_entrada(nAlternativas, gabarito):
        return 'false'
    if not validar_entrada(nAlternativas, resposta):
        return 'false'
    x = ""
    nAcertos = 0
    nAlternativasCertas = 0
    nota = 100
    gabaritoBin = format(gabarito, "b")
    respostaBin = format(resposta, "b")

    for i in range(nAlternativas - len(gabaritoBin)):
        x = x + "0"

    gabaritoBin = x + gabaritoBin
    x = ""
    for i in range(nAlternativas - len(respostaBin)):
        x = x + "0"

    respostaBin = x + respostaBin

    for i in range(nAlternativas):
        if (gabaritoBin[i] == "0" and respostaBin[i] == "1"):
            nota = 0
            break
        elif (gabaritoBin[i] == "1"):
            nAlternativasCertas += 1
            if (respostaBin[i] == "1"):
                nAcertos += 1

    if (nota != 0):
        nota = nAcertos / nAlternativasCertas

    return nota


def corrigirMetodo2(gabarito, resposta, nAlternativas):
    gabarito = int(gabarito)
    resposta = int(resposta)

    if not validar_entrada(nAlternativas, gabarito):
        return False
    if not validar_entrada(nAlternativas, resposta):
        return False

    x = ""
    ntpc = 0  # número total de proposições corretas
    npc = 0  # número proposições corretas assinaladas
    npi = 0  # número de porsições incorretas consideradas corretas

    gabaritoBin = format(gabarito, "b")
    respostaBin = format(resposta, "b")

    for i in range(nAlternativas - len(gabaritoBin)):
        x = x + "0"
    gabaritoBin = x + gabaritoBin
    x = ""
    for i in range(nAlternativas - len(respostaBin)):
        x = x + "0"
    respostaBin = x + respostaBin

    for i in range(nAlternativas):
        if (gabaritoBin[i] == "1"):
            ntpc += 1
            if (respostaBin[i] == "1"):
                npc += 1
        else:
            if (respostaBin[i] == "1"):
                npi += 1

    if (npc > npi):
        nota = (nAlternativas - (ntpc - (npc - npi))) / nAlternativas
    else:
        nota = 0

    return nota


def validar_entrada(n_alternativas, valor):
    x = 0
    for i in range(n_alternativas):
        x = x + 2 ** i
    if valor>x:
        return False
    else:
        return True


if __name__ == "__main__":
    r = corrigirMetodo2(21,13,5)



