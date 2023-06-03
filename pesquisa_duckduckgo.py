def pesquisa_duduckgo():
    # API DE BUSCA DE IMAGENS
    from duckduckgo_search import ddg_images

    # BIBLIOTECA QUE USAREMOS PARA CONVERTER A COR DAS IMAGENS E SALVÁ-LAS
    import cv2
    # BIBLIOTECA PARA LER IMAGENS DE UM LINK
    from skimage import io
    # BIBLIOTECA QUE USAREMOS PARA MANIPULAR DIRETÓRIOS
    import os

    pergunta = True

    while pergunta:

        pesquisa = str(input('Digite sua pesquisa de imagens: '))

        # REALIZA A PESQUISA COM BASE NA PALAVRA-CHAVE
        resultado_pesquisa = ddg_images(pesquisa)

        # TENTA LER A QUANTIDADE DE ARQUIVOS HÁ NO DIRETÓRIO E CASO NÃO EXISTA O DIRETÓRIO ELE CRIA
        try:
            num_arquivos_pasta = len(os.listdir('Dados'))
        except:
            os.mkdir('Dados')
            num_arquivos_pasta = 0

        # LAÇO PARA VARRER TODOS OS ELEMENTOS DO RESULTADO DA PESQUISA
        if resultado_pesquisa:
            for aux in range(len(resultado_pesquisa)):
                try:
                    # LÊ O LINK DA IMAGEM
                    link = io.imread(f'{resultado_pesquisa[aux]["image"]}')

                    # CONVERTE A COR DE BGR PARA RGB
                    img = cv2.cvtColor(link, cv2.COLOR_BGR2RGB)

                    # SALVA AS IMAGENS NO DIRETÓRIO
                    cv2.imwrite(f'Dados/{num_arquivos_pasta}.jpg', img)

                    num_arquivos_pasta += 1
                except:
                    pass
        else:
            print('Não foi possível realizar a pesquisa')

        opcao = str(input('Deseja continuar baixando imagens?\n1 - Sim\n2 - Não\n: '))

        while opcao != '1' and opcao != '2':

            if opcao != '1' and opcao != '2':
                print('Resposta inválida!\n')
                opcao = str(input('Deseja continuar baixando imagens?\n1 - Sim\n2 - Não\n: '))

        match opcao:

            case '1':
                pergunta = True

            case '2':
                break
