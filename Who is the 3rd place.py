def third_place(names, scores):
    # Membuat pasangan nama dan skor
    participants = list(zip(names, scores))

    # Mengurutkan peserta berdasarkan skor (descending order)
    sorted_participants = sorted(participants, key=lambda x: x[1], reverse=True)

    # Menemukan nilai terbaik ketiga
    third_place_score = sorted(set(scores), reverse=True)[2]

    # Memilih peserta yang mendapat nilai terbaik ketiga
    third_place_winners = [name for name, score in sorted_participants if score == third_place_score]

    # Menghasilkan output
    output = 'The third winner: ' + ', '.join(third_place_winners)

    return output

# Example 1
names1 = ['Andi', 'Budi', 'Charlie', 'Dilan', 'Echa']
scores1 = [80, 90, 95, 100, 85]
result1 = third_place(names1, scores1)
print(result1)

# Example 2
names2 = ['Andi', 'Budi', 'Charlie', 'Dilan', 'Echa']
scores2 = [80, 80, 80, 100, 90]
result2 = third_place(names2, scores2)
print(result2)

# Example 3
names3 = ['Andi', 'Budi', 'Charlie', 'Dilan', 'Echa', 'Fanya']
scores3 = [80, 90, 90, 100, 100, 80]
result3 = third_place(names3, scores3)
print(result3)
