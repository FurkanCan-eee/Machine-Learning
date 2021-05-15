
##############################################################################
# Kütüphanelerin yüklenmesi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# Verilerin okunması

veriler = pd.read_csv("Wine.csv")
print(veriler)

print()

X = veriler.iloc[:,0:13].values
Y = veriler.iloc[:,13].values

##############################################################################
# Veri kümesinin eğitim ve test kümeleri olarak bölünmesi

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.33, random_state = 0)

##############################################################################
# Öznitelik ölçekleme ( verileri birbirlerine yakın olacak şekilde ölçekleme )( Her zaman kullanılmak zorunda değil )

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

##############################################################################
# Boyut indirgeme / Principal Component Analysis (PCA) algoritması oluşturma

from sklearn.decomposition import PCA

pca = PCA(n_components=2)  # veriyi 13 boyuttan 2 boyuta indirgemek

X_train2 = pca.fit_transform(X_train)  # X_test verileri, X_train ile aynı boyutlara
X_test2 = pca.transform(X_test)  # sahip olsun diye üstte fit edilmiş sınıfı altta transform ediyoruz.

##############################################################################
# Logostic Regression uygulamak

# PCA uygulanmadan önce logistic regression
from sklearn.linear_model import LogisticRegression

logr_pca = LogisticRegression(random_state=0)
logr_pca.fit(X_train,y_train)

# PCA uygulandıktan sonra logistic regression
logr2_pca = LogisticRegression(random_state=0)
logr2_pca.fit(X_train2,y_train)

# Tahminler
y_pred = logr_pca.predict(X_test)

y_pred2 = logr2_pca.predict(X_test2)

# Confusion matrix oluşturma
from sklearn.metrics import confusion_matrix

# Actual / PCA uygulanmadan önceki confusion matrix
print("Actual/PCA olmadan")
cm = confusion_matrix(y_test,y_pred)
print(cm)

# Actual / PCA uygulandıktan sonraki confusion matrix
print("Actual/PCA ile")
cm2 = confusion_matrix(y_test,y_pred2)
print(cm2)

# PCA olmadan / PCA uygulandıktan sonraki confusion matrix
print("Actual/PCA ile")
cm3 = confusion_matrix(y_pred,y_pred2)
print(cm3)
