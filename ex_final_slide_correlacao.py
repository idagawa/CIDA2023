# Importação das bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Entrada de dados (via arquivo .csv)
arquivo = "C:\\Users\\professor\\Desktop\\dados_corr.csv"
dados_originais = pd.read_csv(arquivo, header=0)
dados_dict = dados_originais.to_dict('list')

# Processamento dos dados
matriz_corr = [dados_dict["altura"], dados_dict["lado"],
               dados_dict["processo"], dados_dict["massa"]]

# Linearização
tamanho = len(dados_dict["altura"])
contador = range(tamanho)
altura_log = []
lado_log = []
processo_log = []
massa_log = []
for i in contador:
    valor = np.log(dados_dict["altura"][i])
    altura_log.append(valor)

    valor = np.log(dados_dict["lado"][i])
    lado_log.append(valor)

    valor = np.log(dados_dict["processo"][i])
    processo_log.append(valor)

    valor = np.log(dados_dict["massa"][i])
    massa_log.append(valor)

matriz_corr_linearizada = [altura_log, lado_log,
                           processo_log, massa_log]

rho_linearizado = np.corrcoef(matriz_corr_linearizada)

# Cálculo da correlação linear de Pearson
rho = np.corrcoef(matriz_corr)

# Apresentação dos resultados
print(dados_dict)
print(matriz_corr)
print("Resultados da correlação linear:")
print(rho)
print(rho_linearizado)

# Verificação dos resultados (fazer as dispersões)
graf1 = plt.scatter(dados_dict["altura"], dados_dict["massa"])
plt.title("Massa em função da altura")
plt.xlabel("altura")
plt.ylabel("massa")
plt.show()

graf2 = plt.scatter(dados_dict["lado"], dados_dict["massa"])
plt.title("Massa em função do lado")
plt.xlabel("lado")
plt.ylabel("massa")
plt.show()






