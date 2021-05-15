##############################################################################
# Öznitelik ölçekleme ( verileri birbirlerine yakın olacak şekilde ölçekleme )( Her zaman kullanılmak zorunda değil )

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

# Verileri normalize etmek

from sklearn.preprocessing import Normalizer

norm = Normalizer()

X_train_norm = norm.fit_transform(x_train)
X_test_norm = norm.fit_transform(x_test)
