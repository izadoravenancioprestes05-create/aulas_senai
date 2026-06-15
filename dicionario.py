# **Kwargs - armumentos nomeados variaveis
#Capitura qualquer quantidade de argumentos como um dicionario valor1 [0]

def exibir_info(**dados): # ** Kwargs vira dicionário
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
    
exibir_info(nome = "Carlos", idade= 30, cidade = "SP", partido= "Bolsonaro")

