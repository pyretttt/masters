import numpy as np

x = np.uint8(-456)
print(x)

x = np.array([
    [1, 2],
    # [3, 4],
    # [6, 7]
])

print('Размерность массива: ', x.ndim)
print('Форма массива ', x.shape) # for 1 dimensional return number of columns, 
                                # for 2 dimensional return rows X columns, 
                                # for 3 dimensional depth x rows x columns

r = np.arange(2.5, 5.0, 0.5, dtype=np.float16)
print(r) # Can accept float numbers

l, step = np.linspace(-6, 21, 60, retstep=True, endpoint=False) # start, end (inclusive), number of elements will be equally distributed, retstep - return tuple with step
print(l, 'step ', step)


z = np.random.sample((3, 4)) * 100
print(z)

w = np.random.randint(0, 11, (3, 4)) # start, exclusive end, matrix shape
print(w)

k = np.array([
    [2, 2],
    [4, 8]
])
print(k.mean(axis=1))

