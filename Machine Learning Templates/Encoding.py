##############################################################################
# Encoding: Katagorik veriler => Numeric veriler -- Yöntem 1--

ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)

##############################################################################
# Encoding: Katagorik veriler => Numeric veriler -- Yöntem 2--

from sklearn.preprocessing import LabelEncoder

# Bu tek satırla tüm kolonlara LabelEncoder uygulanabiliyor.
veriler2 = veriler.apply(LabelEncoder().fit_transform)

c = veriler2.iloc[:,:1]
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
c=ohe.fit_transform(c).toarray()
print(c)
