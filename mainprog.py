#Trabalho covid
#!!!!!Usando tabela temporaria pq arquivo ta muito grande heuheueh

def arquivoLista():
    lines = []
    with open("tabelatemp.txt",'r') as file:
        for line in file: 
            line = line.replace('\n', '')
            lines.append(line)
        del lines [0]
    return lines

def porcentagem(parte,inteiro):
    percentual = ( int(parte) / int(inteiro) ) * 100
    return percentual

def calculoQtd(list):
    quantity = 0
    for item in list:
        quantity += 1
    return quantity

def listaHomens(lista):
    homens = []
    for item in lista:
        if 'Masculino' in item:
            homens.append(item)
    return homens

def listaMulheres(lista):
    mulheres = []
    for item in lista:
        if 'Feminino' in item:
            mulheres.append(item)
    return mulheres

def listaPositivo(lista):
    final = []
    for item in lista:
        if 'Positivo' in item:
            final.append(item)
    return final

def listaAssintomaticos(lista):
    final = []
    for item in lista:
        if 'Assintomático' in item:
            final.append(item)
    return final

def listaSintomaticos(lista):
    final = []
    for item in lista:
        if 'Assintomatico' not in item:
            final.append(item)
    return final

def acima50(lista):
    final = [] 
    for item in lista:
        number = item[-2]
        if int(number) >= 5:
            final.append(item)
    return final

def abaixo20(lista):
    final = [] 
    for item in lista:
        number = item[-2] + item[-1]
        if int(number) <= 20:
            final.append(item)
    return final

Lista = arquivoLista()
print(abaixo20(Lista))