"""
Group:
Varfolomeeva Viktoria 60
Sineokaya Anastasia 50
"""
import RU_LOCAL as RU
from textblob import TextBlob
from deep_translator import GoogleTranslator

text = input(RU.INTRO)
text_letters = text
text_orig = text
count_vowels = 0
count_alpha = 0
summ_ord = 0

for i in range(len(text)):
    if text[i].isalpha():
        count_alpha += 1
        summ_ord += ord(text[i])

average = summ_ord / count_alpha
if average <= 122:
    lang = 'eng'
else:
    lang = 'ru'

text = text.split(' ')
count_words = len(text)

text_letters = text_letters.lower()
if lang == 'ru':
    count_vowels = text_letters.count('а') + text_letters.count('о') + text_letters.count('у') + text_letters.count(
        'ы') + text_letters.count('э') + text_letters.count('е') + text_letters.count('ё') + text_letters.count(
        'и') + text_letters.count('ю') + text_letters.count('я')
elif lang == 'eng':
    count_vowels = text_letters.count('a') + text_letters.count('e') + text_letters.count('i')\
                   + text_letters.count('o') + text_letters.count('u') + text_letters.count('y')

count_sentences = text_letters.count('.') + text_letters.count('?') + text_letters.count('!')

ASL = count_words / count_sentences
ASW = count_vowels / count_words

if lang == 'ru':
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW
else:
    FRE = 206.835 - 1.015 * ASL - 84.6 * ASW

if FRE > 80:
    result = RU.FRE_JUNIOR
elif FRE > 50:
    result = RU.FRE_PUPILS
elif FRE > 25:
    result = RU.FRE_STUDENTS
else:
    result = RU.FRE_GRADUATE

translated = GoogleTranslator(source='auto', target='en').translate(text_orig)
translated = TextBlob(translated)

pol = translated.sentiment.polarity
if pol <= -1/3:
    pol_ans = RU.POL_NEGATIVE
elif pol <= 1/3:
    pol_ans = RU.POL_NEUTRAL
else:
    pol_ans = RU.POL_POSITIVE

sub = str(translated.sentiment.subjectivity * 100) + '%'

print(RU.SENTENCES, count_sentences)
print(RU.WORDS, count_words)
print(RU.SYLLABLES, count_vowels)
print(RU.AVERAGE_S_L, ASL)
print(RU.AVERAGE_S_W, ASW)
print(RU.FRE, FRE)
print(result)
print(RU.POL, pol_ans)
print(RU.SUB, sub)
