""" variavel que recebe entrada via input e imprime o nome da tela"""

# nomes = input("Digite o seu nome:")
# print("Olá,", nomes)

#Fase 2-lista e laco while
#Agora guarda varios nomes
nomes=[]

#While cria um laco infinito - so para com o "Break"

while True:
    nome = input("Digite um nome (ou 'sair' para terminar):")

    if nome.lower() == 'sair':
        break
    else:
        nomes.append(nome)

for n in nomes:
    print(n)


# Fase 3- Busca de nomes

busca = input("Pesquisar nome: ")

# 'in' verifica se o valor existe dentro da lista

if busca in nomes:
    print(f"{busca} encontrado")

else:
    print(f"{busca} não está na lista") 

# 'for' é usado para percorrer toda a lista(banco de dados)

for i, n in enumerate(nomes, 1):
    print(f"{i}. {n}")


