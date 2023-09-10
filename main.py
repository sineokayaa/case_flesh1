"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""
import RU_LOCAL as RU
from textblob import TextBlob


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

text_letters = text_letters.lower()
print(text_letters)
count_vowels = text_letters.count('а') + text_letters.count('о') + text_letters.count('у') + text_letters.count('ы') + text_letters.count('э') + text_letters.count('е') + text_letters.count('ё') + text_letters.count('и') + text_letters.count('ю') + text_letters.count('я')
print(count_vowels, 'слогов')
#count_vowels = text_letters.count('a') + text_letters.count('e') + text_letters.count('i') + text_letters.count('o') + text_letters.count('u') + text_letters.count('y')
#print(count_vowels, 'слогов')

mid_lenght = text_letters.count('.') + text_letters.count('?') + text_letters.count('!')
print('Слов:', words)
print('Слогов:', count_vowels)
print('Средняя длина предложения в словах:', words/mid_lenght)
print('Средняя длина слова в слогах:', count_vowels/words)

