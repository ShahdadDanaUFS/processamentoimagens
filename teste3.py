import numpy as np

def dft(x):
    N = len(x)
    X = np.zeros(N, dtype=np.complex128)
    
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    
    return X

# Amostras no domínio do tempo
x = np.array([1, 2, 3, 4])

# Calcula a DFT das amostras
X = dft(x)

print("Amostras originais:", x)
print("DFT resultante:", X)
