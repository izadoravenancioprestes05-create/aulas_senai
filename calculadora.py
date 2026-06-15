def estatisticas(*numeros):
    total= sum(numeros)
    media = total/ len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    print (f"Total: {total} | Média: {media:.2f} |  Máximo {maximo}| min: {minimo}")

estatisticas( 10, 20, 30)
estatisticas(53, 68, 80, 90, 46)
estatisticas(70, 89, 49)

#Listas
lista = (80, 90, 95)
estatisticas(*lista)