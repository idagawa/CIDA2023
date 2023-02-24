# Carregamento das bibliotecas
import numpy as np
import statistics as st
import matplotlib.pyplot as plot

# Carregamento dos dados
dados_globais = [988.8, 556.9, 224.6, 210.9, 201.5, 187.7, 151.6, 135.8, 129.8, 119.4,
                 116, 102.3, 101.8, 92.4, 84.7, 83.9, 80.2, 74.7, 72.7, 68.4, 66.8, 66.8,
                 63.7, 62.8, 61.9, 56.2, 54.1, 50.3, 49.7, 46.3]

dados_sudeste = [988.8, 556.9, 210.9, 101.8, 92.4, 84.7, 83.9, 72.7, 68.4, 63.7, 62.8, 50.3, 49.7, 46.3]

# Processamento dos dados (globais)
Q1g = np.percentile(dados_globais, 25, method="averaged_inverted_cdf")
Q2g = np.percentile(dados_globais, 50, method="averaged_inverted_cdf")
Q3g = np.percentile(dados_globais, 75, method="averaged_inverted_cdf")

dq = Q3g - Q1g

limite_inferior_g = np.fmax(dados_globais[-1], Q1g - 1.5*dq)
limite_superior_g = np.fmin(dados_globais[0], Q3g + 1.5*dq)

# Processamento dos dados (sudeste)
Q1s = np.percentile(dados_sudeste, 25, method="averaged_inverted_cdf")
Q2s = np.percentile(dados_sudeste, 50, method="averaged_inverted_cdf")
Q3s = np.percentile(dados_sudeste, 75, method="averaged_inverted_cdf")

dq = Q3s - Q1s

limite_inferior_s = np.fmax(dados_sudeste[-1], Q1s - 1.5*dq)
limite_superior_s = np.fmin(dados_sudeste[0], Q3s + 1.5*dq)

# Calculo do boxplot
diagrama_global = plot.boxplot(dados_globais, labels=["Brasil!!!"], positions=[1], whis=5)
diagrama_sudeste = plot.boxplot(dados_sudeste, labels=["Sudeste!!!"], positions=[2], whis=5)

# Apresentação dos dados
print("Dados globais:")
print("Q1 = ", Q1g)
print("Q2 = ", Q2g)
print("Q3 = ", Q3g)

print("limite inferior = ", limite_inferior_g)
print("limite superior = ", limite_superior_g)

print("Dados sudeste:")
print("Q1 = ", Q1s)
print("Q2 = ", Q2s)
print("Q3 = ", Q3s)

print("limite inferior = ", limite_inferior_s)
print("limite superior = ", limite_superior_s)

plot.title("Boxplot da distribuição das populações!!!!")
plot.xlabel("Diferentes populações")
plot.ylabel("Número de habitantes")
plot.show()