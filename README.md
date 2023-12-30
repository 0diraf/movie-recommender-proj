
![myke-simon-atsUqIm3wxo-unsplash](https://github.com/0diraf/movie-recommender-proj/assets/139581253/de230104-8539-448c-bd0e-e73b9e770a26)

# Content-based Movie Recommender with Frontend

## :white_check_mark: Objectives

* Explore MovieLens dataset
* Preprocess and transform the dataset for utilization in a content-based recommender system
* Implement content-based recommendation function with cosine distance
* Create a [front-end](https://diraf-mrecommender.streamlit.app/) with intuitive UI for easier access and use.

****

Written in python using pandas, numpy, and sklearn.

This movie recommender uses TheMovieLens dataset which contains movie titles as well as their tag scores. After merging and preprocessing, the final dataset contains around 13k+ observations with 1100+ features. Principal component analysis is performed to select the features that are responsible for 95% of the variation. 

cosine similarity=cos(θ)=A×B||A||.||B|| \text{cosine similarity} = cos(\theta) = \frac{A \times B}{||A|| . ||B||}

1−cosine similarity=cosine distance1 - \text{cosine similarity} = \text{cosine distance} 

Based on the resulting dataset, a cosine distance matrix is calculated in which the observation in the ith row and jth column represents the cosine distance of ith movie from the jth movie and vice versa. 

After a movie title is inputted and the number of recommendations (k) to be obtained is specified, the movie recommender returns k nearest movies to the inputted movie.

Finally, I created a front-end with Streamlit where this movie recommendation engine can be used. [You can access it by clicking here.](https://diraf-mrecommender.streamlit.app/). The webapp queries themoviedb.org database with the name of the movie and it's release year (if listed) to fetch the movie description and poster.

Note: The webapp may be put to sleep due to inactivity. You may have to wake it up to access it. Git LFS quota may exceed at some point which may result in deployment errors.
