"""
SOFTWARE CRIADO POR: MARCOS VINÍCIUS ELIAS NERES BARRETO FERREIRA

PYTHON VERSION: 3.11
"""




from baixar_imagens import baixar_imagens
from mudar_nome_arquivo import mudar_nome_arquivo
from trocar_num_classes import trocar_num_classes
from criar_teste_treino import criar_teste_treino
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('=' * 40, '\n', ' ' * 10, 'FERRAMENTAS')
print('=' * 40, '\n')

opcao = str(input('1 - Baixar Imagens\n2 - Mudar Nome de Arquivos\n3 - Trocar as Classes dos Arquivos\n'
                  '4 - Criar Arquivos para Teste e para Treino\n\n: '))

while opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':

    opcao = str(input('1 - Baixar Imagens\n2 - Mudar Nome de Arquivos\n3 - Trocar as Classes dos Arquivos\n'
                      '4 - Criar Arquivos para Teste e para Treino\n\n: '))

    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':

        print('Resposta inválida\n')

match opcao:

    case '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        baixar_imagens()

    case '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        mudar_nome_arquivo()

    case '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        trocar_num_classes()

    case '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        criar_teste_treino()

