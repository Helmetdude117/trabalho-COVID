#IGNORA

lista = [1,2,3]
listab = [1,2,4]

def repetidos(lista1, lista2):
    final = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                final.append(lista1[i])
    return final
                
print(repetidos(lista,listab))