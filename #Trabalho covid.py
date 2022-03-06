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
    return '(' + str(percentual) + '%)'

def calculoQtd(list):
    quantity = 0
    for i in list:
        quantity += 1
    return quantity

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

def finder(Lista, parametro):
    res = []
    for item in Lista:
        if parametro in item:
            res.append(item)
    return res

def main():
    Lista = arquivoLista()
    Total_pessoas = calculoQtd(Lista)
    Homens = finder(Lista, 'Masculino')
    Mulheres = finder(Lista, 'Feminino')
    Positivos = finder(Lista, 'Positivo')
    Assint = finder(Lista, 'Assintomático')
    Sintom = listaSintomaticos(Lista)
    acimacinq = acima50(Lista)
    abaixovin = abaixo20(Lista)
    print('O total de pessoas que fizeram o teste foi:', Total_pessoas)
    print('O total de pessoas do sexo masculino foi:' , calculoQtd(Homens), porcentagem(calculoQtd(Homens),Total_pessoas))
    print('O total de pessoas do sexo feminino foi:' , calculoQtd(Mulheres), porcentagem(calculoQtd(Mulheres), Total_pessoas))
    print('Total de pessoas que testaram positivo:', calculoQtd(Positivos))
    print('Homens que testaram positivo:', calculoQtd(finder(Homens, 'Positivo')))
    print('Mulheres que testaram positivo:' , calculoQtd(finder(Mulheres, 'Positivo'))) 
    print('Pessoas que usaram o teste tipo RT-PCR:' , calculoQtd(finder(Lista, 'RT-PCR')))
    print('Pessoas que usaram o teste tipo teste rápido - anticorpo:' , calculoQtd(finder(Lista, 'R�PIDO - ANTICORPO')))
    print('Total pessoas assintomaticas: ' , calculoQtd(Assint))
    print('Total pessoas que sentiram febre:' , calculoQtd(finder(Lista, 'Febre')))

    
    
    
main()