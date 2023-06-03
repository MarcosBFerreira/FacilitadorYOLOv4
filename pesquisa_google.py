def pesquisa_google():

    # BIBLIOTECA QUE USAREMOS PARA MANIPULAR DIRETÓRIOS
    import os

    # API DE BUSCA DE IMAGENS
    from icrawler.builtin import GoogleImageCrawler

    # BIBLIOTECA PARA PARALIZAR O PROGRAMA
    import time

    pergunta = True

    while pergunta:

        # QUAL BUSCADOR USAREMOS
        pesquisa = GoogleImageCrawler(storage={'root_dir': 'Dados'})

        # PERGUNTA A PALAVRA-CHAVE QUE IREMOS BUSCAR
        pesquisas = str(input('Digite sua pesquisa de imagens: '))

        # ATÉ QUANTAS IMAGENS PODEMOS BAIXAR
        num_imagens = int(input('Digite até quantas imagens podem ser baixadas: '))

        try:
            num_arquivos_dir = len(os.listdir('Dados'))
        except:
            num_arquivos_dir = 0

        if num_arquivos_dir == 0:
            pesquisa.crawl(keyword=pesquisas, max_num=num_imagens, filters={'type': 'photo'})
        else:
            pesquisa.crawl(keyword=pesquisas, max_num=num_imagens + num_arquivos_dir, filters={'type': 'photo'})

        time.sleep(1)

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
