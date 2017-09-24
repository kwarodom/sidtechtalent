import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("train.csv")

#sns.lmplot('GrLivArea', 'SalePrice', data=data, fit_reg=False)
#plt.show()

data['Normalized_Area'] = (data['GrLivArea'] - data['GrLivArea'].mean())/data['GrLivArea'].std()

#Grab the relevant data, scale the predictor variable for the gradient descent...
x = data['Normalized_Area']
y = data['SalePrice']

#GRADIENT DESCENT

alpha = 0.0005 #Step size
iterations = 50000 #No. of iterations
m = y.size #No. of data points
np.random.seed(123) #Set the seed
theta = np.random.rand(2) #Pick some random values to start with

print(theta)

nx = np.array(x)
ny = np.array(y)
#cost = (alpha/m)*np.array(theta[0]+theta[1]*nx-ny).sum()
#cost = (1/(2*m))*np.array((theta[0]+theta[1]*x-y)^2).sum()
#print(m)
#print(cost)

#cost = (1/(2*m))*np.array(pow((theta[0]+theta[1]*nx-ny),2)).sum()
eps = 5
prev_theta = np.copy(theta)
for i in range(iterations):
    theta[0] = theta[0] - (alpha/m)*np.array(theta[0]+theta[1]*nx-ny).sum()
    theta[1] = theta[1] - (alpha/m)*np.array((theta[0]+theta[1]*nx-ny)*nx).sum()
    cost = (1/(2*m))*np.array(pow((theta[0]+theta[1]*nx-ny),2)).sum()
    #print("theta0 = {}, theta1 = {}, cost = {}".format(theta[0],theta[1],cost))
    if abs(theta[0]-prev_theta[0]) < eps and abs(theta[0]-prev_theta[0]) < eps:
        print("exsit at iterations = {}".format(i))
        break
    else:
        prev_theta = np.copy(theta)


    #print(theta)

print(theta)

x_line = np.linspace(-3, 10, 100)
y_line = theta[0] + theta[1] * x_line
sns.lmplot('Normalized_Area', 'SalePrice', data=data, fit_reg=False)
plt.plot(x_line, y_line, 'r')
plt.show()

#
# # GRADIENT DESCENT
# def gradient_descent(x, y, theta, iterations, alpha):
#     """
#     TODO: Implement the algorithm
#     Pseudocode
#     for i to iterations
#         compute current cost value
#         compute gradients
#         update theta => thetha = thetha - alpha * gradient
#     return theta and cost
#     """
#     #

#
#     return theta, cost
#
#
# # Pass the relevant variables to the function and get the new values back...
# #theta, cost = gradient_descent(x, y, theta, iterations, alpha)
#
# # Print the results...
# #print("Gradient Descent: {:.2f}, {:.2f}".format(theta[0], theta[1]))