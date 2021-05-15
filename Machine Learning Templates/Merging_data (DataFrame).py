##############################################################################
# Verilerin birleştirilmesi ve DataFrame oluşturulması

# dataframe oluşturulması
sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ["fr","tr","us"])
print(sonuc1)

sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ["boy","kilo","yas"])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ["cinsiyet"])
print(sonuc3)

# verilerin birleştirilmesi
s1 = pd.concat([sonuc1,sonuc2],axis = 1) 
print(s1)

s2 = pd.concat([s1,sonuc3], axis = 1)
print(s2)
