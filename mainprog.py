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

def finder2(Lista, parametro1, parametro2):
    res = []
    for item in Lista:
        if parametro1 and parametro2 in Lista:
            res.append(item)
    return res

def NOTfinder(lista,parametro):
    final = []
    for item in lista:
        if parametro not in item:
            final.append(item)
    return final

def repetidos(lista1, lista2):
    final = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                final.append(lista1[i])
    return final

def main():
    Lista = arquivoLista()
    Total_pessoas = calculoQtd(Lista)
    Homens = finder(Lista, 'Masculino')
    Mulheres = finder(Lista, 'Feminino')
    Positivos = finder(Lista, 'Positivo')
    Assint = finder(Lista, 'Assintomático')
    Sintom = NOTfinder(Lista, 'Assintomático')
    acimacinq = acima50(Lista)
    abaixovin = abaixo20(Lista)
    mulheres50anos = finder(acimacinq, 'Feminino')
    homens50anos = finder(acimacinq, 'Masculino')
    assint_50 = repetidos(acimacinq, Assint)

    print('Quantidade de pessoas que fizeram o teste:', Total_pessoas)
    print('Quantidade de pessoas do sexo masculino:' , calculoQtd(Homens), porcentagem(calculoQtd(Homens),Total_pessoas))
    print('Quantidade de pessoas do sexo feminino:' , calculoQtd(Mulheres), porcentagem(calculoQtd(Mulheres), Total_pessoas))
    print('Quantidade de pessoas que testaram positivo:', calculoQtd(Positivos), porcentagem(calculoQtd(Positivos), Total_pessoas))
    print('Quantidade de homens que testaram positivo', calculoQtd(finder(Homens, 'Positivo')), porcentagem(calculoQtd(finder(Homens, 'Positivo')),Total_pessoas))
    print('Quantidade de mulheres que testaram positivo:' , calculoQtd(finder(Mulheres, 'Positivo')), porcentagem(calculoQtd(finder(Mulheres, 'Positivo')), Total_pessoas)) 
    print('Quantidade de pessoas que fizeram o teste do tipo “RT-PCR”:' , calculoQtd(finder(Lista, 'RT-PCR')), porcentagem(calculoQtd(finder(Lista, 'RT-PCR')), Total_pessoas))
    print('Quantidade de pessoas que fizeram o teste do “teste rápido – anticorpo”:' , calculoQtd(finder(Lista, 'RÁPIDO - ANTICORPO')), porcentagem(calculoQtd(finder(Lista, 'RÁPIDO - ANTICORPO')), Total_pessoas))
    print('Quantidade de pessoas assintomáticas:' , calculoQtd(Assint), porcentagem(calculoQtd(Assint),Total_pessoas))
    print('Quantidade de pessoas que relataram ter sentido febre:' , calculoQtd(finder(Lista, 'Febre')))
    print('Quantidade de pessoas que relataram ter sentido dor de cabeça:', calculoQtd(finder(Lista, 'Dor de Cabeça')))
    print('Quantidade de pessoas que relataram ter sentido dor de garganta:', calculoQtd(finder(Lista, 'Dor de Garganta')))
    print('Quantidade de mulheres, acima de 50 anos, assintomáticas:', calculoQtd(finder(assint_50,'Feminino')), porcentagem(calculoQtd(finder(assint_50,'Feminino')), Total_pessoas) )
    print('Quantidade de homens, acima de 50 anos, assintomáticos:' , calculoQtd(finder(assint_50,'Masculino')), porcentagem(calculoQtd(finder(assint_50,'Masculino')), Total_pessoas)  )
    print('Quantidade de pessoas com menos de 20 anos sintomáticos:', calculoQtd(finder(abaixovin, 'Assintomático')), porcentagem(calculoQtd(finder(abaixovin, 'Assintomático')), Total_pessoas))
    print('Quantidade de sintomáticos na cidade de São Paulo:', calculoQtd(finder(Sintom, 'São Paulo')), porcentagem(calculoQtd(finder(Sintom,'São Paulo')), Total_pessoas))
    print('Quantidade de mulheres sintomáticas na cidade de Dracena:', calculoQtd(finder(Sintom, 'Feminino')), porcentagem(calculoQtd(finder(Sintom, 'Feminino')),Total_pessoas))
    print('Quantidade de homens, maiores de 50 anos, sintomáticos na cidade de Bauru:', calculoQtd(finder(homens50anos, 'Bauru')), porcentagem(calculoQtd(finder(homens50anos, 'Bauru')), Total_pessoas))
    
    
main()