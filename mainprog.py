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
    homens50anos = finder(acimacinq, 'Masculino')

    print('Quantidade de pessoas que fizeram o teste:', Total_pessoas)
    print('Quantidade de pessoas do sexo masculino:' , calculoQtd(Homens), porcentagem(calculoQtd(Homens),Total_pessoas))
    print('Quantidade de pessoas do sexo feminino:' , calculoQtd(Mulheres), porcentagem(calculoQtd(Mulheres), Total_pessoas))
    print('Quantidade de pessoas que testaram positivo:', calculoQtd(Positivos))
    print('Quantidade de homens que testaram positivo', calculoQtd(finder(Homens, 'Positivo')))
    print('Quantidade de mulheres que testaram positivo:' , calculoQtd(finder(Mulheres, 'Positivo'))) 
    print('Quantidade de pessoas que fizeram o teste do tipo “RT-PCR”:' , calculoQtd(finder(Lista, 'RT-PCR')))
    print('Quantidade de pessoas que fizeram o teste do “teste rápido – anticorpo”:' , calculoQtd(finder(Lista, 'RÁPIDO - ANTICORPO')))
    print('Quantidade de pessoas assintomáticas:' , calculoQtd(Assint))
    print('Quantidade de pessoas que relataram ter sentido febre:' , calculoQtd(finder(Lista, 'Febre')))
    print('Quantidade de pessoas que relataram ter sentido dor de cabeça:', calculoQtd(finder(Lista, 'Dor de Cabeça')))
    print('Quantidade de pessoas que relataram ter sentido dor de garganta:', calculoQtd(finder(Lista, 'Dor de Garganta')))
    print('Quantidade de mulheres, acima de 50 anos, assintomáticas:')
    print('Quantidade de mulheres, acima de 50 anos, assintomáticos:')
    print('Quantidade de pessoas com menos de 20 anos sintomáticos:')
    print('Quantidade de sintomáticos na cidade de São Paulo:')
    print('Quantidade de mulheres sintomáticas na cidade de Dracena:')
    
main()