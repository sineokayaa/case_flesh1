"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""
import RU_LOCAL as RU
from textblob import TextBlob
from deep_translator import GoogleTranslator

text = input(RU.intro)
text_letters = text
text_orig = TextBlob(text)
lang = ''
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
count_vowels = text_letters.count('а') + text_letters.count('о') + text_letters.count('у') + text_letters.count(
    'ы') + text_letters.count('э') + text_letters.count('е') + text_letters.count('ё') + text_letters.count(
    'и') + text_letters.count('ю') + text_letters.count('я')
print(count_vowels, 'слогов')
# count_vowels = text_letters.count('a') + text_letters.count('e') + text_letters.count('i') + text_letters.count('o') + text_letters.count('u') + text_letters.count('y')
# print(count_vowels, 'слогов')


mid_lenght = text_letters.count('.') + text_letters.count('?') + text_letters.count('!')

ASL = words / mid_lenght
ASW = count_vowels / words

if lang == 'ru':
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW
else:
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW

if FRE > 80:
    result = RU.FRE_junior
elif FRE > 50:
    result = RU.FRE_pupils
elif FRE > 25:
    result = RU.FRE_students
else:
    result = RU.FRE_graduate

translated = GoogleTranslator(source='auto', target='en').translate(text_orig)

pol = translated.sentiment.polarity
if pol <= -1/3:
    pol_ans = RU.pol_negative
elif pol <= 1/3:
    pol_ans = RU.pol_neutral
else:
    pol_ans = RU.pol_positive

sub = str(translated.sentiment.subjectivity * 100) + '%'

print('Слов:', words)
print('Слогов:', count_vowels)
print('Средняя длина предложения в словах:', ASL)
print('Средняя длина слова в слогах:', ASW)
print(RU.FRE, FRE)
print(result)
print(RU.pol, pol_ans)
print(RU.sub, sub)
