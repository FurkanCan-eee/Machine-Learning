##############################################################################
# Logistic Regression sınıflandırma (classification) algoritması oluşturma

from sklearn.linear_model import LogisticRegression

logr = LogisticRegression(random_state=0)
logr.fit(x_train,y_train)

y_pred = logr.predict(x_test)
