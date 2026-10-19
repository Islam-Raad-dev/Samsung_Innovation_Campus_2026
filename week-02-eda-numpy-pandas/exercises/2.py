import numpy as np

arr2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print(f"Number of dimensions: {arr2d.ndim}")
print(arr2d)


print("*" * 20)


arr3d = np.array(
    [
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
    ]
)
print(f"Number of dimensions: {arr3d.ndim}")
print(arr3d)


print("*" * 20)


arr4d = np.array(
    [
        [
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
            [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]],
        ],
        [
            [[31, 32, 33, 34, 35], [36, 37, 38, 39, 40], [41, 42, 43, 44, 45]],
            [[46, 47, 48, 49, 50], [51, 52, 53, 54, 55], [56, 57, 58, 59, 60]],
        ],
    ],
    dtype=int,
)
print(f"Number of dimensions: {arr4d.ndim}")
print(arr4d)

# _______________________________________________________________________

print("*" * 20)

arr5 = np.reshape(arr2d, (5, 3))
print(f"Number of dimensions: {arr5.ndim}")
print(arr5)

# ________________________________________________________________________

print("*" * 20)

data = np.random.randn(2, 3)
print(f"Random numbers from a normal distribution:\n {data}")

mean = np.mean(data)
print(f"Mean of the random numbers: {mean}")

#_________________________________________________________________________

print("*" * 20)