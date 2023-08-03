#LISTS EM PYTHON 
#.insert(0,x) coloca na posicao desejada
#for it para listas 
#.sort()- organiza a lista


"""numero=[]
num = soma = 0
for i in range (0,15,1):
    print("Digite um numero: ")
    num = int(input())
    numero.append(num)
for i in numero :
    soma += i
print(f"Soma: {soma}")"""


"""      #import statistics
numero= []
num = media = 0.0
soma = 0.0
#digitando os numeros
for i in range (0,20,1):
    print("Digite um numero real: ")
    num = float(input())
    numero.append(num) # add na lista
#media = statistiscs.mean(numero)
# soma os numeros digitados um por um 
for i in numero:
    soma +=i
media = soma / len(numero)   # soma e divide pelo tanta do numeros(20)
print ("A média dos números digitados é {}".format(media))       """


#FUNCAO PARA CALCULAR RESTO
def resto(n1,n2):
    rs1 = n1 // n2
    rs2 = n2 * rs1
    rs3 = n1 - rs2
    return rs3

#calculo da conta da divisao 
print("Digite 2 numeros inteiros: ")
num1 = int(input())
num2 =int( input() )
resultado= resto(num1,num2)
print(f'Resto : {resultado}')


