from dictogram import Dictogram

def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data)-2):
        if data[i] in markov_model:
            markov_model[data[i]].update([(data[i+1], data[i+2])])
            #markov_model[data[i]].update([data[i+1]]) # чтобы сделать цепь 1 порядка
        else:
            markov_model[data[i]]= Dictogram([(data[i+1], data[i+2])])
            #markov_model[data[i]]= Dictogram([data[i+1]]) # чтобы сделать цепь 1 порядка
    return markov_model

