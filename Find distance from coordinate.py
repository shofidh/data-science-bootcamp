import math

def distance(point_1, point_2):
    # Hitung jarak menggunakan rumus Euclidean
    distance_value = math.sqrt((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)
    
    # Buat output dengan format jarak
    output = f'The distance is {distance_value}'

    return output

# Contoh penggunaan
point_1 = [5, 5]
point_2 = [1, 2]
print(distance(point_1, point_2))  # Output: 'The distance is 5.000000'

point_1 = [0, -1]
point_2 = [-3, 2]
print(distance(point_1, point_2))  # Output: 'The distance is 4.242641'
