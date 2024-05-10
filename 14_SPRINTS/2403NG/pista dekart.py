# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wF58BdR4-QOGYBT_dLLUHmpaeI1eCfZU
"""

import statistics as st
# Dados de consumo de energia em kWh
consumo_energia = ([20, 25, 30, 35, 40])

# Calculando a média
media = st.mean(consumo_energia)

# Calculando a variância
variancia = st.mean(consumo_energia)

# Exibindo os resultados
print(f"Média do consumo de energia: {media} kWh")
print(f"Variância do consumo de energia: {variancia} kWh^2")

"""# MEDIA"""

def ft_media(lista):
  soma =0
  for i in lista:
    soma = soma + i
  media = soma/len(lista)
  return media

import statistics as st

# Dados do atleta
tempo_atleta = [10, 15, 20, 25, 30]

# Cálculo da média
media = st.mean(tempo_atleta)

# Melhor tempo (o menor tempo)
melhor_tempo = min(tempo_atleta)

# Exibindo os resultados
print(f"O tempo médio da corrida do atleta é: {media}")
print(f"O melhor tempo da corrida do atleta é: {melhor_tempo}")
import numpy as np

def melhor_volta(corredores):
    melhor_corredor, melhor_volta = min(corredores.items(), key=lambda x: min(x[1]))
    return melhor_corredor, min(melhor_volta), melhor_volta.index(min(melhor_volta)) + 1

def volta_media_rapida(corredores):
    tempos_por_volta = {volta: np.mean([corredores[corredor][volta - 1] for corredor in corredores]) for volta in range(10)}
    return min(tempos_por_volta, key=tempos_por_volta.get), min(tempos_por_volta.values())

def main():
    corredores = {}
    nomes_corredores = ["tiago", "thaisa", "ale", "gabriel", "tom", "franci"]
    
    for nome in nomes_corredores:
        tempos = [float(input(f"Digite o tempo da {volta}ª volta (em segundos) para o corredor {nome}: ")) for volta in range(1, 11)]
        corredores[nome] = tempos
    
    melhor_corredor, melhor_tempo, melhor_volta = melhor_volta(corredores)
    print(f"\nMelhor volta: {melhor_corredor}, {melhor_tempo} segundos, na volta {melhor_volta}.")
    
    volta_media_numero, volta_media = volta_media_rapida(corredores)
    print(f"\nVolta com a média mais rápida: {volta_media_numero}, com média de {volta_media} segundos.")
    
    classificacao = sorted(corredores.items(), key=lambda x: sum(x[1]))
    print("\nClassificação final em ordem crescente:")
    for posicao, (corredor, tempos) in enumerate(classificacao, start=1):
        print(f"{posicao}. {corredor} - Tempo total: {sum(tempos)} segundos")

main()
