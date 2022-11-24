# Segementer Report

The two segmenters I am using for the comparison are the Pragmatic Segmenter and the Punkt Segmenter from NLTK.

Pragmatic segmenter is a rule-based sentence boundary detection system. The pragmatic segmenter is made to work across multiple different languages even when the format and domain is unknown. The pragmatic segmenter does not use any machine-learning techniques. The pragmatic segmenter does use regular expression and it is written in Ruby. The segmenter correctly identifies 71 out of 73 sentences but introduces mistakes such as considering citations as sentences at times thereby increasing the number of lines.for example - [35]: 121  is considered as a line but original text - 91–92  for similar counterprogramming.[35]: 121 . The sentences where Pragmatic segmenter gets wrong are where citations and sentence boundaries come together along with some numbers.


The punkt segmenter divides a text into a list of sentences by using an unsupervised learning algorithm to build a model for abbreviations, collocations, and words that start a sentence. The punkt segmenter must be trained on a large collection of text from the target language before it can be used. The punkt segementer uses regular expressions and it is written in Python. The segmenter correctly identifies all the sentences but similar to pragmatic segmenter, punkt also considers some citations as sentences.
