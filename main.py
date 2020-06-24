
import codecs
import generator
import models
import re
import random

#reading from files
with codecs.open('original.txt', 'r', encoding='utf-8') as scource_file: 
    origin_text = scource_file.read()

#making magic
total_text = []
scource_text = re.split(r' ', origin_text)
text_model = models.make_markov_model(scource_text)
text_lenght = random.randint(1, 150)
# print(text_model)
for i in range(text_lenght):
    sentence = generator.generate_random_sentence(text_model)
    total_text.append(sentence)


# writing generated text
with codecs.open('words.txt', 'w', encoding='utf-8') as total_words:
    for sentence in total_text:
        total_words.write(sentence)
