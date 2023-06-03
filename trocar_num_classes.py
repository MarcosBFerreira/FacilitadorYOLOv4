"""SOFTWARE CRIADO POR ÁTILA DA SILVA AGUIAR, YAN RIBEIRO DE PAIVA E MARCOS VINÍCIUS ELIAS NERES BARRETO FERREIRA
PARA AUTOMATIZAR A TROCA DE CLASSES DAS REFERÊNCIAS GERADAS PELO LABELIMG

VERSÃO PYTHON: 3.9 e 3.11
"""


def trocar_num_classes():

    import os

    pasta_referencias = str(input('Digite o caminho da pasta onde estão apenas as referências: '))
    num_letra = int(input('Digite o número a qual a letra da classe representa: '))
    num_letra -= 1
    arquivos = os.listdir(pasta_referencias)

    for nome_arquivo in range(0, len(arquivos)):

        f = open(f'{pasta_referencias}' + '\\' + arquivos[nome_arquivo], 'r')
        g = f'{num_letra} ' + f.readline()[2:]
        f.close()
        f = open(f'{pasta_referencias}' + '\\' + arquivos[nome_arquivo], 'w')
        f.write(g)
        f.close()
