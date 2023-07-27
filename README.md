Written in python using pandas, numpy, and sklearn.

This movie recommender uses TheMovieLens dataset which contains movie titles as well as their tag scores. After merging and preprocessing, the final dataset contains around 13k+ observations with 1100+ features. Principal component analysis is performed to select the features that are responsible for 95% of the variation. 

<p><center> $ cos(\theta) = \frac{A \times B}{||A|| . ||B||} $ </center></p>

Based on the resulting dataset, a cosine distance matrix is calculated in which the observation in the ith row and jth column represents the cosine distance of ith movie from the jth movie and vice versa. After a movie title is inputted and the number of recommendations (k) to be obtained is specified, the movie recommender returns k nearest movies to the inputted movie.

Finally, I created a front-end with Streamlit where this movie recommendation engine can be used. [You can access it by clicking here.](diraf-mrecommender.streamlit.app)
