import numpy as np
from scipy.ndimage import zoom

def enlarge_binary_matrix(binary_matrix, scale_factor):
    # Ensure the matrix is binary (contains only 0s and 1s)
    assert np.all(np.logical_or(binary_matrix == 0, binary_matrix == 1)), "Input matrix must be binary"

    # Use nearest-neighbor interpolation to preserve binary nature
    enlarged_matrix = zoom(binary_matrix, scale_factor, order=0, mode='nearest')

    # Round the values to ensure they remain binary
    enlarged_matrix = np.round(enlarged_matrix).astype(int)

    return enlarged_matrix

# Generate a random binary matrix
original_matrix = np.random.choice([0, 1], size=(5, 5), p=[0.5, 0.5])

scale_factor = 2  # You can adjust this based on your requirements
enlarged_matrix = enlarge_binary_matrix(original_matrix, scale_factor)

print("Original Matrix:")
print(original_matrix)
print("\nEnlarged Matrix:")
print(enlarged_matrix)

