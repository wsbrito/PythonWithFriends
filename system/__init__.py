'''
Arquivo de inicialização do sistema. Aqui sera lido o arquivo de configuracao config.json
e executada a rotina para criacao da base de dados do sistema e de testes
'''
import json
from classes.model.database import *

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

#print(data)
criar_banco_de_dados(data['diretorio_banco_de_dados'], data['nome_banco_de_dados'], False)

criar_banco_de_dados(data['diretorio_banco_de_dados_teste'], data['nome_banco_de_dados_teste'], True)

