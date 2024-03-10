import math

def square_root(a, b, c):
    # Menghitung diskriminan
    discriminant = b**2 - 4*a*c
    
    # Periksa kondisi solusi
    if discriminant > 0:
        # Dua solusi riil
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        output = f'X1 = {x1}, X2 = {x2}'
    elif discriminant == 0:
        # Satu solusi riil
        x = -b / (2*a)
        output = f'X = {x}'
    else:
        # Tidak ada solusi riil
        output = 'No solution'
    
    return output

# Contoh penggunaan
print(square_root(1, -5, 6))  # Output: 'X1 = 3.0, X2 = 2.0'
print(square_root(2, 4, 2))    # Output: 'X = -1.0'
print(square_root(1, 1, 9))    # Output: 'No solution'
