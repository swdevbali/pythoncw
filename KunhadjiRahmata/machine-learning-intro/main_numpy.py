import numpy as np

# Ciptakan array dengan list of list
np_array = np.array(
    [
        [ 0, 1, 2, 3, 4],
        [ 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14]
    ]
)

print(np_array.ndim, np_array.shape)

np_array_2d = np.array([(1.5,2,3), (4,5,6)], dtype=float)

# Buat Ukuran
array_zero =np.zeros((3, 4))
print(array_zero.ndim, array_zero.shape)
print(array_zero)

# Buat Ukuran 2x3x4 dengan isi 1
array_ones = np.ones( (2,3,4), dtype=np.int16)
print(array_ones)

# Array Kosong 2x3 array
array_kosong = np.empty((2, 3))
print(array_kosong)

### Menciptakan array dengan pola tertentu
# Array 1D dengan bilangan dari 10 s/d 30 dengan kenaikan 5
array_1d = np.arange( 10, 30, 5)

# Array 1D dengan Bilangan daro 0 s/d 2 dengan kenaikan 0.3
array_1d = np.arange(0, 2, 0.3)

# Membuat Array 1D dengan 9 bilangan, dengan jarak merata dari
array_1d = np.linspace(0, 2, 9)
print(array_1d)
print(array_1d.ndim, array_1d.shape)
