##############################################################################
# Polynomial Regression / Doğrusal olmayan (nonlinear model) oluşturma 

from sklearn.preprocessing import PolynomialFeatures

# 2.dereceden polinom
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)

lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,Y)
