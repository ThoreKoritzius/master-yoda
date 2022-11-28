# Master Yoda
Natural Language Processing (NLP) is an interesting field and I wanted to experiment a bit with it. <br> By using Spacy and POS-tagging one can build a dependency tree of a given sentence.<br>
This allows for the fun idea of re-arranging words in the way Master Yoda would say them:

Examples:
>"The universe is big" -> "big The universe   is"

>"I love good coding" -> "good coding  I  love"

>"You are the best" - > "the best  You  are"

Usage
--
> pip install spacy

call the ```speak(sentence)``` method with your sentence and just execute the python file