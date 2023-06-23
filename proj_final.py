# Importação das bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

# Carregamento dos dados
arquivo = "C:\\Users\\professor\\Desktop\\dados_motor.csv"
dados_originais = pd.read_csv(arquivo, header = 1)  # leitura no formato dataframe
dados_dict = dados_originais.to_dict("list")        # converte para dicionário

# Processamento dos dados
total_dados = 14
posicao_inicial = 1

dict_selecionado = {"PC": [],
                    "TA": []}

contador = range(posicao_inicial, posicao_inicial+total_dados)

# Programação do item (a)
for i in contador:
    dict_selecionado["PC"].append(dados_dict["Pressao Combustivel"][i])
    dict_selecionado["TA"].append(dados_dict["Temperatura Arrefecimento"][i])

# Programação do item (b)
k = 1.0 + 3.32*np.log10(total_dados)    # Número de barras do histograma
numero_bins = int(np.round(k))          # Arredonda o numero de barras para um inteiro
plt.hist(dict_selecionado["PC"], numero_bins)
plt.xlabel("Pressão do Combustível")
plt.ylabel("Quantidade")
plt.title("Histograma da pressão do combustível para os dados selecionados")
plt.show()

# Programação do item (c)
Q2 = np.percentile(dict_selecionado["TA"], 50, method="averaged_inverted_cdf")
plt.boxplot(dict_selecionado["TA"])
plt.ylabel("Temperatura de Arrefecimento")
plt.title("Boxplot da temperatura de arrefecimento para os dados selecionados")
plt.show()

# Programação do item (d)
dict_cond_motor = {"OK": [],
                   "ruim": []}

tamanho_total = len(dados_originais["Condicao Motor"])
contador = range(tamanho_total)
for i in contador:
    if (dados_originais["Condicao Motor"][i] == 0):
        dict_cond_motor["ruim"].append(dados_originais["Rotacao"][i])
    else:
        dict_cond_motor["OK"].append(dados_originais["Rotacao"][i])

plt.boxplot(dict_cond_motor["ruim"], positions=[0], labels=["Motor Ruim"])
plt.boxplot(dict_cond_motor["OK"], positions=[1], labels=["Motor OK"])
plt.ylabel("Rotação (RPM)")
plt.title("Comparação entre os boxplots da rotação em função da condição do motor")
plt.show()

# Programação do item (e)
tamanho_total = len(dados_originais["Rotacao"])
k = 1.0 + 3.32*np.log10(tamanho_total)    # Número de barras do histograma
numero_bins = int(np.round(k))          # Arredonda o numero de barras para um inteiro

plt.hist(dados_originais["Rotacao"], numero_bins)
plt.xlabel("Rotação (RPM)")
plt.ylabel("Quantidade")
plt.title("Histograma da rotação de todos os dados")
plt.show()

# Programação do item (f)
matriz_linear = [dados_originais["Rotacao"], dados_originais["Pressao Oleo"], dados_originais["Pressao Combustivel"],
                 dados_originais["Pressao Arrefecimento"], dados_originais["Temperatura Oleo"],
                 dados_originais["Temperatura Arrefecimento"]]
rho = np.corrcoef(matriz_linear)

print("Matriz de correlação linear de Pearson")
print(rho)

rotulos = ["Rotacao", "P. Óleo", "P. Combustível", "P. Arrefecimento", "Temp. Óleo", "Temp. Arrefecimento"]
snb.heatmap(rho, annot=True, xticklabels=rotulos, yticklabels=rotulos)
plt.show()

# Programação do item (g)
tamanho_total = len(dados_originais["Rotacao"])
contador = range(tamanho_total)

rot_linearizado = []
po_linearizado = []
pc_linearizado = []
pa_linearizado = []
to_linearizado = []
ta_linearizado = []

for i in contador:
    if ((dados_originais["Rotacao"][i] > 0.0) and (dados_originais["Pressao Oleo"][i] > 0.0) and
            (dados_originais["Pressao Combustivel"][i] > 0.0) and (dados_originais["Pressao Arrefecimento"][i] > 0.0) and
            (dados_originais["Temperatura Oleo"][i] > 0.0) and (dados_originais["Temperatura Arrefecimento"][i] > 0.0)):
        rot_linearizado.append(np.log10(dados_originais["Rotacao"][i]))
        po_linearizado.append(np.log10(dados_originais["Pressao Oleo"][i]))
        pc_linearizado.append(np.log10(dados_originais["Pressao Combustivel"][i]))
        pa_linearizado.append(np.log10(dados_originais["Pressao Arrefecimento"][i]))
        to_linearizado.append(np.log10(dados_originais["Temperatura Oleo"][i]))
        ta_linearizado.append(np.log10(dados_originais["Temperatura Arrefecimento"][i]))

matriz_linearizada = [rot_linearizado, po_linearizado, pc_linearizado, pa_linearizado, to_linearizado, ta_linearizado]
rho_linearizado = np.corrcoef(matriz_linearizada)

print("Matriz de correlação linearizada")
print(rho_linearizado)

snb.heatmap(rho_linearizado, annot=True, xticklabels=rotulos, yticklabels=rotulos)
plt.show()
