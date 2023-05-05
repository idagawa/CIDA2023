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
razaoK = []
tamanho = len(dados_dict["Amostra"])
contador = range(tamanho)
for i in contador:
    valor = dados_dict["d"][i]/dados_dict["h"][i]
    razaoR.append(valor)

    valor = dados_dict["d"][i] * dados_dict["h"][i]
    razaoK.append(valor)

# Fazer a matriz de correlação de Pearson
matriz_correlacao = [dados_dict["Porca"], dados_dict["h"],
                     dados_dict["d"], dados_dict["m"],
                     razaoR, razaoK]
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
media_porcas = np.mean(dados_dict["Porca"])
media_alturas = np.mean(dados_dict["h"])
alfa = []   # calcula Xi-Xmedia
beta = []   # calcula Yi-Ymedia
tamanho = len(dados_dict["Porca"])
contador = range(tamanho)
for i in contador:
    valor = dados_dict["Porca"][i] - media_porcas
    alfa.append(valor)      # preenche a lista alfa
    valor2 = dados_dict["h"][i] - media_alturas
    beta.append(valor2)

soma_numerador = 0.0
soma_denominador = 0.0
for i in contador:
    valor = alfa[i]*beta[i]
    soma_numerador = soma_numerador + valor
    valor = alfa[i]*alfa[i]
    soma_denominador = soma_denominador + valor

# Determinação dos coeficientes do modelo linear
a = soma_numerador/soma_denominador
b = media_alturas - (a * media_porcas)

# Verificação do modelo
teste_porcas = [4, 5, 8, 10, 12, 14, 18, 20, 24, 27, 30]
h_modelo = []
tamanho = len(teste_porcas)
contador = range(tamanho)
for i in contador:
    valor = a*teste_porcas[i] + b
    h_modelo.append(valor)


# Aplicar o MMQO para obter o modelo de d x porca
media_porcas = np.mean(dados_dict["Porca"])
media_diametros = np.mean(dados_dict["d"])
alfa = []   # calcula Xi-Xmedia
beta = []   # calcula Yi-Ymedia
tamanho = len(dados_dict["Porca"])
contador = range(tamanho)
for i in contador:
    valor = dados_dict["Porca"][i] - media_porcas
    alfa.append(valor)      # preenche a lista alfa
    valor2 = dados_dict["d"][i] - media_diametros
    beta.append(valor2)

soma_numerador = 0.0
soma_denominador = 0.0
for i in contador:
    valor = alfa[i]*beta[i]
    soma_numerador = soma_numerador + valor
    valor = alfa[i]*alfa[i]
    soma_denominador = soma_denominador + valor

# Determinação dos coeficientes do modelo linear
a2 = soma_numerador/soma_denominador
b2 = media_diametros - (a2 * media_porcas)

# Verificação do modelo
teste_porcas = [4, 5, 8, 10, 12, 14, 18, 20, 24, 27, 30]
d_modelo = []
tamanho = len(teste_porcas)
contador = range(tamanho)
for i in contador:
    valor = a2*teste_porcas[i] + b2
    d_modelo.append(valor)

# Última regressão linear para obter o modelo m X k
media_massas = np.mean(dados_dict["m"])
media_k = np.mean(razaoK)
alfa = []   # calcula Xi-Xmedia
beta = []   # calcula Yi-Ymedia
tamanho = len(dados_dict["m"])
contador = range(tamanho)
for i in contador:
    valor = razaoK[i] - media_k
    alfa.append(valor)      # preenche a lista alfa
    valor2 = dados_dict["m"][i] - media_massas
    beta.append(valor2)

soma_numerador = 0.0
soma_denominador = 0.0
for i in contador:
    valor = alfa[i]*beta[i]
    soma_numerador = soma_numerador + valor
    valor = alfa[i]*alfa[i]
    soma_denominador = soma_denominador + valor

# Determinação dos coeficientes do modelo linear
a3 = soma_numerador/soma_denominador
b3 = media_massas - (a3 * media_k)

# Verificaçao do modelo
teste_k = [10, 50, 100, 500, 700]
k_modelo = []
tamanho = len(teste_k)
contador = range(tamanho)
for i in contador:
    valor = a3 * teste_k[i] + b3
    k_modelo.append(valor)


# Apresentação dos resultados
print(dados_dict)
print("Matriz de correlação linear: ")
print(rho)
print("Matriz de correlação linearizada: ")
print(rho_linearizado)

print("Modelo para a h X porca: ")
print("a = ", a)
print("b = ", b)

print("teste_modelo = ", teste_porcas)
print("h_modelo = ", h_modelo)

print("Modelo para d X porca: ")
print("a2 = ", a2)
print("b2 = ", b2)


print("Modelo para m X k: ")
print("a3 = ", a3)
print("b3 = ", b3)

# Plot do modelo e dos dados
graf_h_real = plt.scatter(dados_dict["Porca"],
                          dados_dict["h"])
graf_h_modelo = plt.plot(teste_porcas, h_modelo)
plt.title("Comparação modelo X real")
plt.xlabel("Porca")
plt.ylabel("h")
plt.show()

graf_d_real = plt.scatter(dados_dict["Porca"],
                          dados_dict["d"])
graf_d_modelo = plt.plot(teste_porcas, d_modelo)
plt.title("Comparação modelo X real")
plt.xlabel("Porca")
plt.ylabel("d")
plt.show()

# Plot dos gráficos de dispersão
graf1 = plt.scatter(dados_dict["Porca"], dados_dict["m"])
plt.title("Massa em função da porca")
plt.xlabel("Tipo de porca")
plt.ylabel("Massa")
plt.show()
'''
graf2 = plt.scatter(dados_dict["h"], dados_dict["m"])
plt.title("Massa em função da altura")
plt.xlabel("h")
plt.ylabel("Massa")
#plt.show()

graf3 = plt.scatter(dados_dict["d"], dados_dict["m"])
plt.title("Massa em função do diâmetro")
plt.xlabel("d")
plt.ylabel("Massa")
#plt.show()

graf4 = plt.scatter(dados_dict["Porca"], dados_dict["h"])
plt.title("h em função do tipo de porca")
plt.xlabel("Porca")
plt.ylabel("h")
#plt.show()

graf5 = plt.scatter(dados_dict["Porca"], dados_dict["d"])
plt.title("D em função do tipo de porca")
plt.xlabel("Porca")
plt.ylabel("D")
#plt.show()
'''
graf6 = plt.scatter(razaoK, dados_dict["m"])
graf7 = plt.plot(teste_k, k_modelo)
plt.title("Massa da porca em função de K")
plt.xlabel("K")
plt.ylabel("Massa")
plt.show()
