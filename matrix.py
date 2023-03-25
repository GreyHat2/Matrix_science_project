#matrix.py

import numpy as np

ALPHABET_SIZE = 27
MATRIX_SIZE = 2

SMALL_ALPHABET = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
CAPITAL_ALPHABET = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ALPHABET_VALUES = list(range(ALPHABET_SIZE))

def string_to_values(input_string):
    values = []
    for char in input_string:
        if char in SMALL_ALPHABET:
            values.append(ALPHABET_VALUES[SMALL_ALPHABET.index(char)])
        elif char in CAPITAL_ALPHABET:
            values.append(ALPHABET_VALUES[CAPITAL_ALPHABET.index(char)])
        else:
            raise ValueError(f"Invalid character '{char}' in input string")
    return values

def pad_values(values):
    if len(values) % MATRIX_SIZE == 1:
        values.append(ALPHABET_VALUES[0])
    return values

def values_to_matrix(values):
    n = len(values) // MATRIX_SIZE
    return np.array(values[:n*MATRIX_SIZE]).reshape((MATRIX_SIZE, n))

def matrix_to_values(matrix):
    return matrix.flatten().tolist()

def encrypt(input_string, encoding_matrix):
    values = string_to_values(input_string)
    padded_values = pad_values(values)
    matrix = values_to_matrix(padded_values)
    encrypted_matrix = np.matmul(encoding_matrix, matrix)
    encrypted_values = matrix_to_values(encrypted_matrix)
    return encrypted_values

def decrypt(encrypted_values, encoding_matrix):
    decrypted_values = np.matmul(np.linalg.inv(encoding_matrix), np.array(encrypted_values).reshape((MATRIX_SIZE, -1)))
    decrypted_values = [int(round(val)) for val in decrypted_values.flatten()]
    decrypted_values = [val % ALPHABET_SIZE for val in decrypted_values]
    decrypted_string = "".join([SMALL_ALPHABET[val] for val in decrypted_values])
    return decrypted_string





        # a, b, c, d = map(int, input("Enter the encoding matrix as comma-separated values: ").split(","))
        # encoding_matrix = np.array([[a, b], [c, d]])
        # encrypted_values = list(map(int, input("Enter the encrypted form matrix as comma-separated values: ").split(",")))
        # decrypted_string = decrypt(encrypted_values, encoding_matrix)
        # print(f"Decrypted form = {decrypted_string}")
