words = input().split()

even_length_words = [word for word in words if len(word) % 2 == 0]
print(*even_length_words, sep="\n")