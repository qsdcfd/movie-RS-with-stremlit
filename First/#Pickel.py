#Pickel
import pickle
import pandas as pd

movies = df2[['id', 'title']].copy()
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)


pickle.dump(movies, open('movies.pickle', 'wb'))
pickle.dump(cosine_sim2, open('cosine_sim.pickle', 'wb'))