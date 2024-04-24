sentence = "This is a common interview question"
char_counts = dict()
for char in sentence:
    if char.lower() in char_counts:
        char_counts[char.lower()] += 1
    else:
        char_counts[char.lower()] = 1

print(char_counts)
max_num = 0
letter = ''
for key in char_counts:
    if char_counts[key] > max_num:
        max_num = char_counts[key]
        letter = key

print(letter, max_num)

print(char_counts.items())
char_frequency_sorted = sorted(
    char_counts.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[0])
