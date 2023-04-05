# Carregamento das bibliotecas
import matplotlib.pyplot as plot
import numpy as np

# Importação dos dados
dados = [2, 3, 4, 5, 5, 5, 5, 6, 7, 8,
         8, 8, 9, 10, 10, 12, 12, 14, 14, 14,
         16, 20, 23, 25, 25, 28, 30, 32, 35, 38]

# Processamento dos dados
# Determinação da quantidade de classes (por Sturges)
qtd_dados = len(dados)  # tamanho dos dados
k = 1 + 3.32 * np.log10(qtd_dados)  # acha o no. de classes
k = np.round(k)     # arredonda para um no. inteiro

# Extração dos dados de clases e frequências
qtd, classes = np.histogram(dados, bins=int(k))
#_, retorno2 = np.histogram(dados, bins=int(k))     # Grava apenas o 2o retorno

# Apresentação dos resultados
print("Numero de classes = ", k)
print("Classes: ", classes)
print("Quantidades: ", qtd)
#print("Apenas o 2o retorno: ", retorno2)
diagrama = plot.hist(dados, bins=int(k))
plot.show()

#diagrama = plot.boxplot(dados)
#plot.show()
