# Grafik gösterimi

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.plot(x_train, y_train)
plt.plot(x_test, tahmin)

plt.title("Title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
