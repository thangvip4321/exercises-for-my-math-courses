from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt 
data,target = fetch_olivetti_faces(return_X_y = True)

extractor = PCA(n_components =0.7)
per_face_features =extractor.fit_transform(data,target)

basis = extractor.components_
mean_face = extractor.mean_
rank = extractor.n_components_
vector_length = np.linalg.norm(basis,axis = 1,ord=2)
print("the length of each vector in the basis is:",vector_length)
covariance_matrix = np.zeros(shape = (rank,rank))
for i in range(covariance_matrix.shape[0]):
	for j in range (covariance_matrix.shape[1]):
		covariance_matrix[i,j] = np.dot(basis[i],basis[j])
print("the inner product of each vector with another one in the basis is",covariance_matrix)

# for the part of verifying each value in coordinate vector equals the inner product of the basis vector 
# and (X-X_mean) , we will only test this one 1 example

difference_vector = [per_face_features[0,i] -np.dot((data[0] - mean_face),basis[i]) for i in range(rank)]
print("so the difference in result between this formula and the standard one in PCA is:",difference_vector)
print("maybe they are just one anyway")