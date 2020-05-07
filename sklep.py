import numpy as np
import matplotlib.pyplot as plt

bufor = 2 #int(input("Podaj wielkosc bufora: "))
intensywnosc =2 #int(input("Podaj intensywnosc naplywu pakietow: "))
obsluga =2 #int(input("Podaj sredni czas obslugi pakietu: "))

a = bufor

matrix = np.zeros((a, a))

itera = 0


lamba = np.arange(0.5, 6.1, 0.1)
mi = 8

et = lamba/mi
print(et)

eb = 1 / (mi - lamba)
print(eb)

plt.plot(lamba, eb)
plt.xlim([0,6.5])
plt.ylim([0.1,0.55])
plt.show()


for i in range(0,a):
    for j in range(0,a):
        if(i==0):
            matrix[i][j] = 1
            continue
        if(i==j):
            matrix[i][j] = 1
            continue
        if(j==i-1):
            if(itera == bufor):
                itera = bufor
            else:
                itera= itera + 1
            matrix[i][j] = -intensywnosc/obsluga
            continue
        matrix[i][j] = 0

# print(matrix)

# print(np.linalg.det(matrix))
print(matrix)

matrixinv = np.linalg.inv(matrix)

# print(matrixinv)

b = np.zeros(a)
b[0] = 1
# print(b)

x = matrixinv @ b

print(x)

print("Szansa ze nie uda sie obsluzyc klienta bo nie bedzie miejsca w kolejce wynosi", x[-1])




