##############################################################################
# Verilerin ölçeklenmesi 
# Support Vector Regression için ölçekleme önemli bir yer tutmaktadır.

from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_ölçekli = sc1.fit_transform(X)

sc2 = StandardScaler()
y_ölçekli = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))

##############################################################################
# SVR modelinin oluşturulması

from sklearn.svm import SVR

svr_reg = SVR(kernel="rbf")
svr_reg.fit(x_ölçekli,y_ölçekli)
