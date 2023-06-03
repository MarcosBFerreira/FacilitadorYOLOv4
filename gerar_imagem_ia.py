def gerar_imagem_ia():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.chromium.service import ChromiumService
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.opera import OperaDriverManager
    from skimage import io
    import cv2
    import os
    import time

    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        #navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    except:
        print('Você não tem o Google Chrome instalado')

    try:
        num_arquivos_pasta = len(os.listdir('Dados'))
    except:
        os.mkdir('Dados')
        num_arquivos_pasta = 0
    # INFORMAÇÕES DE LOGIN

    email = 'projetoautomacao2023@hotmail.com'
    senha = '@Projeto2023'

    criar = str(input('Digite o aqui como quer que a imagem seja criada: '))

    print('\nGERANDO AS IMAGENS...')
    time.sleep(5)
    navegador.get('https://www.bing.com/create')
    time.sleep(10)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[2]/button[1]/a').click()
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div/div/div[1]/form/textarea').send_keys(f'{criar}')
    time.sleep(2)
    navegador.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[1]/div/div/a').click()

    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/'
                                     'div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]'
                                     '/div/input[1]').send_keys(f'{email}')

    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/'
                                     'div/div/div/div[4]/div/div/div/div/input').click()
    time.sleep(2)

    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]'
                                     '/div/div[2]/div/div[3]/div/div[2]/input').send_keys(f'{senha}')

    navegador.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div'
                                     '/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').click()

    time.sleep(5)

    navegador.find_element(By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/'
                                     'div/div[2]/div/div[3]/div[2]/div/div/div[1]/input').click()

    time.sleep(20)
    try:
        try:
            # BAIXANDO A PRIMEIRA IMAGEM
            img1 = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[1]/div/div/a/div/img').get_attribute('src')
            link = io.imread(f'{img1}')
            cv2.imwrite(f'Dados/{num_arquivos_pasta}.jpg', cv2.cvtColor(link, cv2.COLOR_BGR2RGB))
        except:
            pass
        try:
            # BAIXANDO A SEGUNDA IMAGEM
            img2 = navegador.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[1]/li[2]/div/div/a/div/img').get_attribute('src')
            link = io.imread(f'{img2}')
            cv2.imwrite(f'Dados/{num_arquivos_pasta + 1}.jpg', cv2.cvtColor(link, cv2.COLOR_BGR2RGB))
        except:
            pass
        try:
            # BAIXANDO A TERCEIRA IMAGEM
            img3 = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[1]/div/div/a/div/img').get_attribute('src')
            link = io.imread(f'{img3}')
            cv2.imwrite(f'Dados/{num_arquivos_pasta + 2}.jpg', cv2.cvtColor(link, cv2.COLOR_BGR2RGB))
        except:
            pass
        try:
            # BAIXANDO A QUARTA IMAGEM
            img4 = navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[1]/div/div/div/ul[2]/li[2]/div/div/a/div/img').get_attribute('src')
            link = io.imread(f'{img4}')
            cv2.imwrite(f'Dados/{num_arquivos_pasta + 3}.jpg', cv2.cvtColor(link, cv2.COLOR_BGR2RGB))
        except:
            pass
    except:
        print('Não conseguimos baixar nenhuma Imagem')












    navegador.close()

    print('\nIMAGENS GERADAS COM SUCESSO')
    a = input('Aperte <ENTER> para sair')