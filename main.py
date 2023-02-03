import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
# import math
# import seaborn as sb
# from scipy import stats
from pandas import read_csv

df = read_csv("movies.csv",header=0,index_col=0)

# print(df)


# inciso 4.2 

# print("¿Cuáles son las 10 películas que más ingresos tuvieron? ")
# indexes = df['budget'].sort_values(ascending=False).head(10).index.to_list()
# results = df.loc[indexes, 'title']
# print(results)
# results2 = df.loc[indexes, 'budget']
# print(results2)


# inciso 4.4

# print("¿Cuál es la peor película de acuerdo a los votos de todos los usuarios?")
# indexes = df['voteAvg'].sort_values().head(1).index.to_list()
# print(indexes)
# results = df.loc[indexes, 'title']
# print(results)
# results2 = df.loc[indexes, 'voteAvg']
# print(results2)

# inciso 4.6

# print("¿Cuál es el género principal de las 20 películas más recientes? ¿Cuál es el género principal que predomina en el conjunto de datos? Represéntelo usando un gráfico")
# indexes = df['releaseDate'] 
# indexes = indexes.apply(pd.to_datetime).sort_values(ascending=False).head(20).index.to_list()
# results = df.loc[indexes, 'genres'].values.tolist()
# results2 = []

# for i in results:
#     if isinstance(i, str):
#         results2.append(i.rsplit('|')[0])
#     else:
#         results2.append('n/a')

# print(f"Generos principales de las 20 peliculas mas recientes:")

# def count_items(l:list, item):
#     return l.count(item)

# final = {}
# labels = set(results2)

# for i in labels:
#     final[i] = count_items(results2,i)

# print(final)

# plt.pie(final.values(),labels=final.keys())
# plt.show()



# inciso 4.8
print("¿La cantidad de actores influye en los ingresos de las películas?\n¿se han hecho películas con más actores en los últimos años?")
# corr_actorsAmont_and_revenue = df['actorsAmount'].corr(df['revenue'])
# print(cor_actorsAmont_and_revenue)
# print(df['revenue'].apply(pd.to_datetime))
df2 = pd.DataFrame()
df2['actors'] = df['actorsAmount']
df2['time'] = pd.to_datetime(df['releaseDate'])
df2['timestamp'] = df2['time'].values.astype(float) # / 10**9
print(df2)
corr = df2['actors'].corr(df2['timestamp'])
print(corr)
# cor_actorsAmont_and_revenue = df['actorsAmount'].corr()
# print(cor_actorsAmont_and_revenue)

# results = df.loc[indexes, 'title']
# print(results)
# results2 = df.loc[indexes, 'voteAvg']
# print(results2)