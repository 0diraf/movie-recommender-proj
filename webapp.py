import streamlit as st
import sys
import pickle
import requests
import time
import gc
from pathlib import Path

pkl_path = Path(__file__).parents[0]

m = pkl_path / "movies_data.pkl"
c = pkl_path / "cosdist_mat.pkl"

def getOverviewAndPoster(title, year):
	if year!=0:
		url = "https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&year={}&language=en-US&page=1".format(title, year)
	else:
		url = "https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&language=en-US&page=1".format(title)
	
	headers = {
	    "accept": "application/json",
	    "Authorization": "Bearer {}".format(st.secrets["api_key"])
	}

	response = requests.get(url, headers=headers)
	i_url = response.json()["results"][0]["poster_path"]
	over = response.json()["results"][0]["overview"]
	url_prefix = "https://image.tmdb.org/t/p/w300_and_h450_bestv2"
	poster_url = url_prefix + i_url
	return poster_url, over

def recommender(k, title, distmatrix):

    neighbors = []
    movie = distmatrix.loc[title].sort_values(axis=0)
    
    for y in range(k):
        neighbors.append(movie.index[y+1])
        
    return neighbors

movies = pickle.load(open(m, "rb"))
distmatrix = pickle.load(open(c, "rb"))
movie_names = movies["title"].values

st.title("Movie Recommendation Engine")

st.write("Written in python using pandas and scipy. Movie data acquired from the MovieLens and preprocessed for the purposes of this engine. Frontend made with streamlit.")

st.text("")

st.markdown("### Movie Recommendation Engine Project")

name = st.selectbox("Movies", movie_names)

st.text("")

m_year = movies.loc[movies.title==name, 'year'].values[0]
image, ov = getOverviewAndPoster(name, m_year)

col1, col2 = st.columns(2)

col1.image(image)
col2.markdown("### {}".format(name))
col2.write(ov)

st.text("")


number = col2.number_input("Number of Recommendations", 0, 10)

if st.button("Recommend Movies"):

	st.text("")

	if number>0:
		r_movies = recommender(number, name, distmatrix)
		for n in r_movies:
			if n!=name:
				n_year = movies.loc[movies.title==n, 'year'].values[0]
				img, over = getOverviewAndPoster(n, n_year)
				col1, col2 = st.columns(2)
				col1.image(img)
				col2.markdown("### {}".format(n))
				col2.write(over)
				st.text("")
			gc.collect()
