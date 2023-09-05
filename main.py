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
for i in range(len(text)):
    if text[i] != '':
        words += 1
