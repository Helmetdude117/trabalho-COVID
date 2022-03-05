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
        
print(arquivoLista())

def porcentagem(parte,inteiro):
    percentual = ( int(parte) / int(inteiro) ) * 100
    return percentual

def quantidadePessoas(list):
    quantity = 0
    for item in list:
        quantity += 1
    return quantity

def quantidadeMasc(list):
    quantity = 0 
    for item in list:
        if 'Masculino' in item:
            quantity += 1
    return quantity
    
