#!/usr/bin/env python
# coding: utf-8

# In[8]:


# !pip install streamlit
# get_ipython().system('pip install "altair<5"')


# In[58]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import operator
import re
import streamlit as st

from scipy import spatial

# get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


movies = pd.read_csv("movies.csv")
tags = pd.read_csv("tags.csv")
links = pd.read_csv("links.csv")
ratings = pd.read_csv("ratings.csv")


# In[4]:


genome_tags = pd.read_csv("genome-tags.csv")
genome_scores = pd.read_csv("genome-scores.csv")


# In[5]:


movies.head()


# In[6]:


len(movies)


# In[7]:


genome_tags.head(20)


# In[8]:


genome_scores.head(20)


# In[9]:


inter_merge = pd.merge(genome_scores, genome_tags, on="tagId")


# In[10]:


inter_merge.head()


# In[11]:


len(inter_merge)


# In[12]:


inter_merge.drop("tagId", axis=1, inplace=True)


# In[13]:


wide = pd.pivot(inter_merge, index="movieId", columns="tag", values="relevance")


# In[14]:


wide.reset_index(inplace=True)
wide.head()


# In[35]:


wide.describe()


# In[15]:


wide = wide.rename_axis(None, axis=1)
wide.head()


# In[16]:


wide=wide.astype(np.float32)


# In[17]:


wide.head()


# In[21]:


len(wide)


# In[193]:


merge = pd.merge(movies, wide, on="movieId")


# In[194]:


merge.head()


# In[20]:


len(merge)


# In[22]:


merge.to_csv("merge.csv", index=False)


# In[71]:


data = pd.read_csv("merge.csv")


# In[72]:


genres_list = list(data["genres"])


# In[73]:


new_genres_list = []
for g in genres_list:
    g = g.split("|")
    new_genres_list.append(g)


# In[74]:


final_genres = []

for l in new_genres_list:
    for g in l:
        final_genres.append(g)

final_genres


# In[75]:


final_genres = list(set(final_genres))


# In[76]:


for i in final_genres:
    data[i] = 0


# In[77]:


for i in final_genres:
    data[i] = data.apply(lambda x: 1 if i in x["genres"] else 0, axis=1)


# In[78]:


data.drop("genres", axis=1, inplace=True)


# In[79]:


data.drop("movieId", axis=1, inplace=True)


# In[80]:


data['title'] = data.title.str.replace(r'\(.*\)', '')
data.head()


# In[81]:


data["title"] = data["title"].str.rstrip()
data.head()


# In[82]:


data.drop("(no genres listed)", axis=1, inplace=True)
final_genres.remove("(no genres listed)")


# In[84]:


data.dropna(inplace=True)
data.drop_duplicates("title", keep="first",inplace=True)


# In[85]:


genres_dict = {}
for i in final_genres:
    count = data[i].sum()
    genres_dict[i] = count


# In[40]:


genre_counts = pd.DataFrame(genres_dict.items())
genre_counts.rename(columns={0:"Genre", 1:"Count"}, inplace=True)


# In[52]:


ax = sns.barplot(data=genre_counts, x="Genre", y="Count", order=genre_counts.sort_values('Count', ascending=False).Genre)
ax.tick_params(axis='x', rotation=90)


# In[90]:


columns = list(data.columns)
tags = columns[1:-19]
genres = columns[-19:]


# In[87]:


def similarityFn(title1, title2):
    first_m = data.loc[data["title"]==title1]
    second_m = data.loc[data["title"]==title2]
    
    genre_sim = spatial.distance.cosine(first_m[genres], second_m[genres])
    tags_sim = spatial.distance.cosine(first_m[tags], second_m[tags])
    
    sim = genre_sim + tags_sim
    return sim


# In[88]:


def neighbors(k, movie):
    
    distances = []
    for t in data.title:
        print("t: ", t)
        print("movie:", movie.title[0])
        if t!=movie.title[0]:
            distance = similarityFn(movie.title[0], t)
            distances.append((t,distance))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    
    for y in range(k):
        neighbors.append(distances[y])
        
    print("Recommended Movies:")
    i = 0
    for n in neighbors:
        i = i + 1
        print("{}.", n[0]).format(i)
        
        


# In[89]:


def recommender():
    movie_name = input("Enter movie name: ")
    k = input("Enter the number of similar movies you want to see: ")
    k = int(k)
    movie_name.title()
    movie = data.loc[data["title"]==movie_name]
    
    neighbors(k, movie)
    
    


# In[81]:


# In[91]:


# In[ ]:




