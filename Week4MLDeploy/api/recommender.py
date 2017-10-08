import numpy as np
import pandas as pd
import sklearn
from sklearn.decomposition import TruncatedSVD


class MovieRecommender():

	def __init__(self):
		self.train()

	def train(self):
		movie_data = pd.read_csv('api/data/movie_data.csv', encoding='latin-1')
		uMatrix = pd.pivot_table(
				movie_data,
				columns='movie title',
				index='user_id',
				values='rating',
				fill_value=0
			)
		X = uMatrix.T
		SVD = TruncatedSVD(n_components=12, random_state=17)
		resultant_matrix = SVD.fit_transform(X)

		# correlation matrix
		self.corrDF = pd.DataFrame(
				np.corrcoef(resultant_matrix),
				columns=uMatrix.columns,
				index=uMatrix.columns
			)

		# popular movie
		self.popularDF = movie_data[['movie title', 'rating']] \
							.groupby('movie title') \
							.sum() \
							.sort_values('rating', ascending=False)

	def recommend(self, movieTitle, n=15):
		if movieTitle in self.corrDF.index:
			return list(
						self.corrDF[movieTitle] \
							.drop(movieTitle) \
							.sort_values(ascending=False) \
							.head(n) \
							.index
					)
		else:
			return list(
						self.popularDF \
							.head(n) \
							.index
					)
