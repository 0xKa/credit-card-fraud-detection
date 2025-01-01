from sklearn.linear_model import LogisticRegression  echo def train_model(X, y):  echo     model = LogisticRegression()  echo     model.fit(X, y)  echo     return model 
