import numpy as np

kasy = int(input("Podaj liczbe kas: "))
przedkasy = int(input("Podaj liczbe miejsc przed kasa: "))
intensywnosc = int(input("Podaj intensywnosc naplywu klientow: "))
obsluga = int(input("Podaj sredni czas obslugi klienta: "))

a = kasy+przedkasy

matrix = np.zeros((a, a))

itera = 0

for i in range(0,a):
    for j in range(0,a):
        if(i==0):
            matrix[i][j] = 1
            continue
        if(i==j):
            matrix[i][j] = 1
            continue
        if(j==i-1):
            if(itera == kasy):
                itera = kasy
            else:
                itera= itera + 1
            matrix[i][j] = -intensywnosc/(obsluga*itera)
            continue
        matrix[i][j] = 0

# print(matrix)

# print(np.linalg.det(matrix))

matrixinv = np.linalg.inv(matrix)

# print(matrixinv)

b = np.zeros(a)
b[0] = 1
# print(b)

x = matrixinv @ b

print(x)

print("Szansa ze nie uda sie obsluzyc klienta bo nie bedzie miejsca w kolejce wynosi", x[-1])




