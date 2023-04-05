# Importação das bibliotecas
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

# Carregamento dos dados
arquivo = "C:\\Users\\professor\\Desktop\\dados_pop.csv"
dados_originais = pd.read_csv(arquivo, header=1)
dados_dict = dados_originais.to_dict("list")

# Processamento dos dados
tamanho = len(dados_dict["Estado"])
contador = range(tamanho)
cidades_sudeste = []    # lista vazia p/ o sudeste

for i in contador:
    if ((dados_dict["Estado"][i] == "SP") or
            (dados_dict["Estado"][i] == "RJ") or
            (dados_dict["Estado"][i] == "MG") or
            (dados_dict["Estado"][i] == "ES")):
        cidades_sudeste.append(dados_dict["População"][i])

# Resolução da parte (b) do exercício: apresentar as 3 cidades
# menos populosas do nordeste
cidades_nordeste = []
pop_nordeste = []
tupla_nordeste = list(zip())    # cria uma lista de tuplas vazia

estados_nordeste = ["MA", "PI", "CE", "RN", "PB", "PE", "AL",
                    "SE", "BA"]

tamanho = len(dados_dict["Estado"])
contador = range(tamanho)
for i in contador:      # percorre todos as cidades do arquivo
    if (dados_dict["Estado"][i] in estados_nordeste):
        t = (dados_dict["População"][i], dados_dict["Município"][i])
        tupla_nordeste.append(t)
#        cidades_nordeste.append(dados_dict["Município"][i])
#        pop_nordeste.append(dados_dict["População"][i])

# Supondo que os dados não são fornecidos de forma ordenada,
# vamos precisar ordenar as cidades por população
# A partir da tupla_nordeste criada anteriormente, vamos ordenar as
# cidades com as suas populações
print("Antes de ordenar: ", tupla_nordeste)
tupla_nordeste.sort()
print("Depois de ordenar: ", tupla_nordeste)

# Apresentação dos resultados
print(dados_dict["População"])
print(cidades_sudeste)

# Impressão das 3 cidades menos populosas
print("Cidades menos populosas do nordeste: ")
print(tupla_nordeste[0], tupla_nordeste[1], tupla_nordeste[2])

diagrama = plot.boxplot(dados_dict["População"], positions=[0], labels=["Brasil!!!"])
diagrama2 = plot.boxplot(cidades_sudeste, positions=[1], labels=["Sudeste!!!"])
plot.show()