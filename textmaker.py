import codecs
import generator
import models
import re
import random

def create_model():
    with codecs.open('original.txt', 'r', encoding='utf-8') as scource_file: 
        original_text = scource_file.read()
    scource_text = re.split(r' ', original_text)
    text_model = models.make_markov_model(scource_text)
    return text_model

def create_text(model):
    total_text = []
    lenght = random.randint(1, 10)
    for i in range(lenght):
        sentence = generator.generate_random_sentence(model)
        total_text.append(sentence)
    return total_text
