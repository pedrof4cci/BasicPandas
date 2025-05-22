import pandas as pd


dados = pd.read_csv('aluguel.csv', sep=';') #chama a base de dados
base_tratada = dados.fillna(0)  #troca os valores null por 0
registros_a_remover = base_tratada.query('Valor == 0 | Condominio == 0').index
base_tratada.drop(registros_a_remover, axis= 0, inplace= True)  #romove as linhas com valor = 0 e condominio = 0
