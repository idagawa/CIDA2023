# Importação das bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Entrada de dados
arquivo = "C:\\Users\\professor\\Desktop\\dados_porcas.csv"
dados_originais = pd.read_csv(arquivo, header=0, sep=';')
dados_dict = dados_originais.to_dict('list')

# Processamento dos dados
razaoR = []
tamanho = len(dados_dict["Amostra"])
contador = range(tamanho)
for i in contador:
    valor = dados_dict["d"][i]/dados_dict["h"][i]
    razaoR.append(valor)

# Fazer a matriz de correlação de Pearson
matriz_correlacao = [dados_dict["Porca"], dados_dict["h"],
                     dados_dict["d"], dados_dict["m"],
                     razaoR]
rho = np.corrcoef(matriz_correlacao)

# Realizar a linearização dos dados
porca_log = []
h_log = []
d_log = []
m_log = []
for i in contador:
    valor = np.log(dados_dict["Porca"][i])
    porca_log.append(valor)

    valor = np.log(dados_dict["h"][i])
    h_log.append(valor)

    valor = np.log(dados_dict["d"][i])
    d_log.append(valor)

    valor = np.log(dados_dict["m"][i])
    m_log.append(valor)

matriz_correlacao_linearizada = [porca_log, h_log, d_log, m_log]
rho_linearizado = np.corrcoef(matriz_correlacao_linearizada)

# Aplicar o MMQO para obter o modelo de h x porca





# Apresentação dos resultados
print(dados_dict)
print("Matriz de correlação linear: ")
print(rho)
print("Matriz de correlação linearizada: ")
print(rho_linearizado)

# Plot dos gráficos de dispersão
graf1 = plt.scatter(dados_dict["Porca"], dados_dict["m"])
plt.title("Massa em função da porca")
plt.xlabel("Tipo de porca")
plt.ylabel("Massa")
plt.show()

graf2 = plt.scatter(dados_dict["h"], dados_dict["m"])
plt.title("Massa em função da altura")
plt.xlabel("h")
plt.ylabel("Massa")
plt.show()

graf3 = plt.scatter(dados_dict["d"], dados_dict["m"])
plt.title("Massa em função do diâmetro")
plt.xlabel("d")
plt.ylabel("Massa")
plt.show()

graf4 = plt.scatter(dados_dict["Porca"], dados_dict["h"])
plt.title("h em função do tipo de porca")
plt.xlabel("Porca")
plt.ylabel("h")
plt.show()

graf5 = plt.scatter(dados_dict["Porca"], dados_dict["d"])
plt.title("D em função do tipo de porca")
plt.xlabel("Porca")
plt.ylabel("D")
plt.show()