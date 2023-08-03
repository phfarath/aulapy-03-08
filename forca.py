import random


p1= "seriguela"
p2= "tangerina"
p3= "carambola"
lista_p=[p1,p2,p3]

f1 = "é uma fruta"
f2 = "possui cores quentes"
f13 = "é diuretica"
f23 = "tem outros nomes"
f33 = "parece uma estrela"

palpites=""
lista_palavra=["_","_","_","_","_","_","_","_","_"]


palavra= random.randint(lista_p)
print('  _______     ')
print(' |/      |    ')
print(' |            ')
print(' |            ')
print(' |            ')
print(' |            ')
print(' |            ')
print('_|___         ')
if palavra==p1:
    print(f'Dica 1: {f1}')
    print(f'Dica 2: {f2}')
    print(f'Dica 3: {f13}')
if palavra==p2:
    print(f'Dica 1: {f1}')
    print(f'Dica 2: {f2}')
    print(f'Dica 3: {f23}')

else:
    print(f'Dica 1: {f1}')
    print(f'Dica 2: {f2}')
    print(f'Dica 3: {f33}')

print("Digite uma letra: ")
chute=input()
str.find(chute) in palavra
if chute not in palavra:
        print('  _______     ')
        print(' |/      |    ')
        print(' |      (_)   ')
        print(' |            ')
        print(' |            ')
        print(' |            ')
        print(' |            ')
        print('_|___         ')

       