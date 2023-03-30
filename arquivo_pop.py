# Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

# Entrada de dados (a partir do arquivo .csv)
arquivo = "C:\\Users\\professor\\Desktop\\dados_pop.csv"
dados_original = pd.read_csv(arquivo, header=1)     # os dados estão no formato "dataframe"
dados_dict = dados_original.to_dict("list")

# Processamento dos dados
populacao_sudeste = []    # lista vazia
tamanho_dados = len(dados_dict["Município"])
contador = range(tamanho_dados)

for i in contador:  # percorre todas as cidades
    if ((dados_dict["Estado"][i] == "RJ") or
        (dados_dict["Estado"][i] == "SP") or
        (dados_dict["Estado"][i] == "ES") or
        (dados_dict["Estado"][i] == "MG")):
        populacao_sudeste.append(dados_dict["População"][i])    # adiciona a população da cidade

# Solução da (b), 3 menores cidades do nordeste
tamanho_dados = len(dados_dict["Município"])
contador = range(tamanho_dados)
estados_nordeste = ["BA", "SE", "AL", "CE", "RN", "MA", "PE", "PI", "PB"]
tupla_nordeste = list(zip())    # cria uma lista de tuplas vazia

for i in contador:  # percorre todas as cidades
    if (dados_dict["Estado"][i] in estados_nordeste):   # testa se ele é do nordeste
        # Cria uma tupla com a sua população e o município
        t = (dados_dict["População"][i], dados_dict["Município"][i])
        tupla_nordeste.append(t)    # coloca a tupla na lista final

# Apresentação dos resultados
print(populacao_sudeste)
print("Tupla antes de ordenar: ", tupla_nordeste)
tupla_nordeste.sort()
print("Tupla depois de ordenar: ", tupla_nordeste)

print("Cidades menos populosas do nordeste:")
print(tupla_nordeste[0], tupla_nordeste[1], tupla_nordeste[2])


diagrama = plot.boxplot(dados_dict["População"], positions=[1],
                        labels=["Brasil!!!"])
diagrama2 = plot.boxplot(populacao_sudeste, positions=[2],
                         labels=["Sudeste!!!"])
plot.title("Comparação entre as distribuições do Brasil e do Sudeste")
plot.ylabel("População")
plot.show()