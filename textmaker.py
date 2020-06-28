import codecs
import generator
import models
import re
import random

def create_model():
    with codecs.open('original.txt', 'r', encoding='utf-8') as scource_file: 
        original_text = scource_file.read()
    total_text = []
    scource_text = re.split(r' ', original_text)
    text_model = models.make_markov_model(scource_text)
    return text_model

def create_text(model):
    # lenght = random.randint(1, 2)
    # for i in range(lenght):
    sentence = generator.generate_random_sentence(model)
    # total_text.append(sentence)
    return sentence

"""
# writing generated text
with codecs.open('words.txt', 'w', encoding='utf-8') as total_words:
    for sentence in total_text:
        total_words.write(sentence)
"""