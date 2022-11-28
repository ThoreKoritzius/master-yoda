"""
Master Yoda: A model that restructues your sentence to speek like yoda

Prerequisites: pip install spacy

Current configuration only supports english sentences, change the spacy_model variable to switch to different model

Created on 20-07-2022
@author: Thore Koritzius
"""

import spacy
import os

spacy_model = "en_core_web_sm"
try:
    nlp = spacy.load(spacy_model)
except Exception as e:
    #download model in case it doesnt exist
    os.system(f'python -m spacy download {spacy_model}')
    nlp = spacy.load(spacy_model)

def get_word_graph(node):
    if node.n_lefts + node.n_rights > 0:
        right = [get_word_graph(child) for child in node.children]
        return  [[node.orth_], right]
    else:
        return node.orth_

def traverse(inp):
    if not any(isinstance(el, list) for el in inp):
        if isinstance(inp, str):
            return inp
        return ' '.join(inp)
    res=''
    for i in range(len(inp)):
        res+=traverse(inp[len(inp)-1-i]) + " "
    return res
        
def mr_yoda(sentence):
    doc = nlp(sentence)
    return traverse([get_word_graph(sent.root) for sent in doc.sents][0])

def speak(sentence):
    print("in:  " + sentence + "\nout: " + mr_yoda(sentence) + "\n")

speak("The universe is big")
speak("I love good coding")
speak("You are the best")
