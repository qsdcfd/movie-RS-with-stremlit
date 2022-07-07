#Demographic Filtering

import pandas as pd
import numpy as np

#Data Merge

df1.columns = ['id', 'title', 'cast', 'crew']
df2 = df2.merge(df1[['id', 'cast', 'crew']], on='id')

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)

pop= df2.sort_values('popularity', ascending=False)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")