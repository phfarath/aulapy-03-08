lista_calculo = [10,9,8,7,6,5,4,3,2]
lista_cpf=[]
cpf = ""
cpf_valido = False

def penultimo_digito():
    soma = 0
    cont= -1
    for i in lista_cpf:
        cont += 1
        digito = int(i)
        cpf_calculo = digito * lista_calculo[cont]
        soma += cpf_calculo
        resto = soma % 11
    if resto < 2:
        digito_valido = 0
    else: 
        digito_valido = resto - 11
        digito_valido= abs(digito_valido)
    if digito_valido == int(cpf[-2]):
        return (digito_valido)
    else:
        return False
        

def ultimo_digito(p_digito=0):
    soma = 0
    cont=0
    lista_calculo.insert(0, 11)
    lista_cpf.append(p_digito)
    for i in lista_cpf:
        digito = int(i)
        cpf_calculo = digito * lista_calculo[cont]
        soma += cpf_calculo
        resto = soma % 11
        cont+=1

    if resto < 2:
        digito_valido = 0
    else: 
        digito_valido = resto - 11
        abs(digito_valido)
    
    if digito_valido == int(cpf[-1]):
        return True
    else:
        return False

    lista_calculo.pop(0)
    lista_cpf.pop(-1)
    


# Programa principal
while not cpf_valido:
    print("Digite seu cpf: ")
    cpf = input()
    if len(cpf)== 11:
        for i in range(0,9):
            lista_cpf.append(cpf[i])

        p_valido = penultimo_digito()
        u_valido = ultimo_digito(p_valido)

        if not p_valido and not u_valido:
            print("cpf invalido, tente novamente")
            lista_cpf=[]
        else:
            print('Seu CPF é válido!')
            break
    else:
        print("cpf invalido, tente novamente 11")
