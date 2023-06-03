"""SOFTWARE CRIADO POR MARCOS VINÍCIUS ELIAS NERES BARRETO FERREIRA
NO INTUITO DE EVITAR DUPLICAÇÃO DE NOME DE ARQUIVOS
VERSÃO PYTHON: 3.11
"""
import os

def mudar_nome_arquivo():

    # BIBLIOTECA PARA MANIPULAR ARQUIVOS E DIRETÓRIOS


    # LEITURA DO CAMINHO ONDE SERÃO ARMAZENADAS OS ARQUIVOS
    caminho_colocar = os.listdir(str(input('Digite o caminho das imagens onde serão colocadas: ')))

    # VENDO A QUANTIDADE DE ITENS QUE HÁ ONDE SERÁ ARMAZENADAS OS ARQUIVOS
    num_arquivos_colocar = len(caminho_colocar)
    i = num_arquivos_colocar

    # LEITURA DO CAMINHO ONDE ESTÃO OS ARQUIVOS
    caminho_mudar = str(input('Digite o caminho das imagens que serão mudadas: '))

    # LISTANDO O DIRETÓRIO ONDE ESTÃO OS ARQUIVOS
    arquivos_mudar = os.listdir(caminho_mudar)

    # CRIANDO UMA IDENTIFICAÇÃO PARA EVITAR DUPLICAÇÃO DE NOMES
    identificador = str(input('Digite como quer identificar o arquivo: '))

    # PERGUNTANDO O TIPO DO ARQUIVO
    tipo_arquivo = str(input('Digite o tipo de arquivo:\nExemplo:\ntxt\npng\njpg\n\n:'))

    print(arquivos_mudar)
    print(i)


    for aux in range(len(arquivos_mudar)):

        # PEGANDO O ANTIGO NOME DO ARQUIVO
        antigo_nome = rf'{caminho_mudar}\{arquivos_mudar[aux]}'

        # CRIANDO O NOVO NOME PARA O ARQUIVO
        novo_nome = rf'{caminho_mudar}\{i}{identificador}.{tipo_arquivo}'

        # RENOMEANDO O ARQUIVO
        os.rename(antigo_nome, novo_nome)
        i += 1
