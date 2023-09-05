"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""
import RU_LOCAL as RU
text = input(RU.intro)
words = 0

text = text.split(' ')
print(text)
print(len(text))

for i in range(len(text)):
    print(text[i])
    if text[i] != '':
        words += 1
        text.pop(i)
print(words)
print(text)