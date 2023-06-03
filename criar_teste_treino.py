"""SOFTWARE DESENVOLVIDO POR MARCOS VINÍCIUS ELIAS NERES BARRETO FERREIRA
NO INTUITO DE AUTOMATIZAR A CRIAÇÃO DOS ARQUIVOS DE TREINO E TESTE DO YOLOv4

VERSÃO PYTHON: 3.9 e 3.11
"""


def criar_teste_treino():

    # BIBLIOTECA PARA MANIPULAR ARQUIVOS E DIRETÓRIOS
    import os

    # PERGUNTANDO ONDE ESTÃO AS IMAGENS
    pasta_imagens = str(input('Digite o caminho da pasta onde estão apenas as imagens: '))

    # PERGUNTANDO ONDE SALVAR OS ARQUIVOS GERADOS PELO PROGRAMA
    onde_salvar = str(input('\nDigite o caminho para onde deve ir o arquivo gerado por este programa: '))

    # LISTARÁ O NOME DE TODOS OS ARQUIVOS QUE HÁ NA PASTA DE IMAGENS
    imagens = os.listdir(pasta_imagens)

    # CRIANDO OS ARQUIVOS DE TREINO E DE TESTE
    training = open(f'{onde_salvar}' + '\\' + 'training.txt', 'w')
    test = open(f'{onde_salvar}' + '\\' + 'test.txt', 'w')

    aux = 0
    contador = len(imagens)

    for i in imagens:

        # SE aux FOR MENOR QUE 20% DO CONTADOR ELE ESCREVERÁ O CAMINHO E OS NOMES DAS IMAGENS NO ARQUIVO DE TESTE
        if aux < contador * 0.2:
            test.write(f'{pasta_imagens}' + '\\' + f'{imagens[aux]}' + '\n')
        # SENÃO ESCREVERÁ NO ARQUIVO DE TREINO
        else:
            training.write(f'{pasta_imagens}' + '\\' + f'{imagens[aux]}' + '\n')

        aux += 1
    # FECHANDO OS ARQUIVOS
    test.close()
    training.close()

