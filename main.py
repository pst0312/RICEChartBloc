
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pdf2image import convert_from_path
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression


# pixel scan pdf
pdf_filepath = '/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf'
# windows
# poppler_path = r"C:\Users\sarah\Desktop\Release-25.12.0-0\poppler-25.12.0\Library\bin
img = convert_from_path(pdf_filepath)
data = [{0, 1, 2, 3, 4}, {10, 20, 30, 40, 50}] # placeholder
for i in range(len(img)):
    img[i].save(f'/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf{i+1}.png', 'PNG')
    str = f'/Users/peterterekhov/PycharmProjects/PythonProject/INTRO PDF/GRANT ANALYSIS PDF LIST.pdf{i+1}.png'
    data.append(str)


df = pd.DataFrame(data)
df.index = [f'PNG{i+1}' for i in range(len(df))]
print(df)
df.to_csv('data.csv')

arr = df.to_numpy()
print(arr)

# ml model -> find trends, predict wavelength indicators
# this involves finding the best hyperparameter with test data..??

# X = df.to_numpy()
# Y = df.to_numpy()
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size = 0.2, random_state = 0)
# print('Train set:', Xtrain.shape, Xtest.shape)
# print('Test set:', Xtest.shape, Ytest.shape)
#
# parameters = {'C':[0.01,0.1,1],
#              'penalty':['l2'],
#              'solver':['lbfgs']}
# parameters = {"C":[0.01,0.1,1],'penalty':['l2'], 'solver':['lbfgs']} # l1 lasso l2 ridge
# lr=LogisticRegression()
#
# logreg_cv = GridSearchCV(lr, parameters, cv=10)
# logreg_cv.fit(Xtrain, Ytrain)
#
# print("Tuned Hyperparameters:",logreg_cv.best_params_)
# print("Accuracy:",logreg_cv.best_score_)
#
# # actual prediction
# predictions = model.predict(X_new)
# print(predictions)