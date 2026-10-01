text = input("Enter your text: ").lower().split()
letters = 0
unique_words = 0
longest_word = ""
shortest_word = ""
for word in text:
    letters += len(word)
    if longest_word == "" or len(word) > len(longest_word):
        longest_word = word
    if shortest_word == "" or len(word) < len(shortest_word):
        shortest_word = word
    if text.count(word) == 1:
        unique_words += 1

print(f"Number of letters: {letters}")
print(f"Number of unique words: {unique_words}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")  