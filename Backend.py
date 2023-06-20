
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#DATAFRAME
df = pd.read_csv(r'C:\movie_dataset.csv')
#print(df.columns)
#print(df.rows)
features = ['keywords','cast','genres','director']
def combine_features(row):
    return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
for feature in features:
    df[feature] = df[feature].fillna('')
    #filling all na with empty string
df["combined_features"] = df.apply(combine_features,axis=1)

#combining the features vertically
cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0] 

movie_user_likes="Interstellar"
movie_index = get_index_from_title(movie_user_likes)
similar_movies =  list(enumerate(cosine_sim[movie_index]))
#gives list of tuples unsorted
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 3 similar movies to "+movie_user_likes+" are:\n")
for MOVIE in sorted_similar_movies:
    print(get_title_from_index(MOVIE[0]))
    i=i+1
    if i>=3: 
        break