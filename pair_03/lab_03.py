#1
# text = input("Введіть текст: ")

# letters = 0
# digits = 0
# spaces = 0
# vowels = 0
# vowel_letters = "аеєиіїоуюя"

# for char in text:
# 	if char.isalpha():
# 		letters += 1
# 	if char.isdigit():
# 		digits += 1
# 	if char == " ":
# 		spaces += 1
# 	if char.lower() in vowel_letters:
# 		vowels += 1

# words = text.split()

# print(len(text))
# print(letters)
# print(digits)
# print(spaces)
# print(vowels)
# print(len(words))

#2
# full_name = input("Введіть ПІБ: ")
# parts = full_name.split()

# if len(parts) == 3:
#     lastname = parts[0]
#     firstname = parts[1]
#     pobatkovi = parts[2]
#     print(f"{lastname.title()} {firstname[0].upper()}.{pobatkovi[0].upper()}.")
# else:
#     print("Будь ласка, введіть ПІБ у форматі: Прізвище Ім'я По батькові")

#3
# text1 = input("Enter your text1: ").lower().replace(" ", "")
# text2 = input("Enter your text2: ").lower().replace(" ", "")

# tempText2 = text2

# if len(text1) != len(text2):
#     print("not an anagram")
# else:
#     for i in text1:
#         if i in tempText2:
#             tempText2 = tempText2.replace(i, "", 1)
#             if len(tempText2) == 0:
#                 print("anagram")
#                 break
#         else:
#             print("no anagram")
#             break

#4
# text = input("Enter your text: ").lower().split()
# letters = 0
# unique_words = 0
# longest_word = ""
# shortest_word = ""

# for word in text:
#     letters += len(word)
#     if longest_word == "" or len(word) > len(longest_word):
#         longest_word = word
#     if shortest_word == "" or len(word) < len(shortest_word):
#         shortest_word = word
#     if text.count(word) == 1:
#         unique_words += 1

# print(f"Number of letters: {letters}")
# print(f"Number of unique words: {unique_words}")
# print(f"Longest word: {longest_word}")
# print(f"Shortest word: {shortest_word}") 

# change_word = input("Enter the word to change: ").lower()
# new_word = input("Enter the new word: ").lower()
# text = [new_word if word == change_word else word for word in text]
# print(" ".join(text))



