##############################################################################
# Veri kümesinin eğitim ve test kümeleri olarak bölünmesi

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s1,sonuc3, test_size = 0.33, random_state = 0)
