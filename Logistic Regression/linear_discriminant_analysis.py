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
# Linear Discriminant Analysis (LDA) algoritmasını oluşturmak

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

lda = LDA(n_components=2)

X_train_lda = lda.fit_transform(X_train,y_train)
X_test_lda = lda.transform(X_test)

##############################################################################
# Logostic Regression uygulamak

logr_lda = LogisticRegression(random_state=0)
logr_lda.fit(X_train_lda,y_train)

# Tahmin yapma
y_pred_lda = logr_lda.predict(X_test_lda)

# Confusion matrix oluşturma

# Orijinal veriler ve LDA uygulandıktan sonraki verilerin confusion matrixi
print("Actual/LDA ile")

# Confusion matrix oluşturma
from sklearn.metrics import confusion_matrix
cm4 = confusion_matrix(y_pred,y_pred_lda)
print(cm4)
