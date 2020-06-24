from dictogram import Dictogram
import random
from collections import deque

def generate_random_start(model):
    return random.choice(list(model.keys()))

def generate_random_sentence(markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    sentence_lenght = random.randint(3, 20)
    for i in range(0, sentence_lenght):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weight_random_word()
        current_word = random_weighted_word
        sentence.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return " ".join(sentence) + ". "
    return sentence
    