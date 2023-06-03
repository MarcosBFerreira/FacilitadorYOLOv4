"""
SOFTWARE CRIADO POR MARCOS VINÍCIUS ELIAS NERES BARRETO FERREIRA
NO DIA 10/05/2023, COM O INTUITO DE AUTOMATIZAR A CRIAÇÃO DE BANCO DE DADOS
PARA O TREINAMENTO DA REDE YOLOv4
COPERADORES: FLÁVIO LUCAS DOS SANTOS BAPTISTA
VERSÃO PYTHON: 3.11
"""


def baixar_imagens():
    import os
    from pesquisa_google import pesquisa_google
    from pesquisa_duckduckgo import pesquisa_duduckgo
    from gerar_imagem_ia import gerar_imagem_ia

    opcao = str(input('Quer pesquisar com:\n\n 1 - Pesquisar com Google [MELHOR PESQUISA]\n'
                      ' 2 - Pesquisar com DuckduckGo\n 3 - Gerar imagem pelo Bing Image Creator\n\n: '))

    while opcao != '1' and opcao != '2' and opcao != '3':

        if opcao != '1' and opcao != '2' and opcao != '3':
            print('Resposta inválida!\n')
            opcao = str(input('Quer pesquisar com:\n 1 - Pesquisar com Google [MELHOR PESQUISA]\n'
                              ' 2 - Pesquisar com DuckduckGo\n 3 - Gerar imagem pelo Bing Image Creator\n\n: '))

    match opcao:

        case '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            pesquisa_google()

        case '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            pesquisa_duduckgo()

        case '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            gerar_imagem_ia()
