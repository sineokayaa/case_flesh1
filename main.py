"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""
import RU_LOCAL as RU

text = input(RU.intro)
text_letters = text
words = 0

text = text.split(' ')
print(text)
print(len(text))


for i in range(len(text)):
    if text[i] != '':
        words += 1
print(words)

vowels = ['a', 'y', 'i', 'o', ' e']
count_w = 0

for i in range(text_letters):
    if text_letters[i] == vowels:
        count_w += 1
