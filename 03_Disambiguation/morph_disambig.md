#Using UDPipe

UDPipe is a trainable pipeline for tokenization, tagging, lemmatization and dependency parsing of CoNLL-U files. UDPipe is language-agnostic and can be trained given annotated data in CoNLL-U format.

Steps followed - 

'''
$ git clone https://github.com/ufal/udpipe
$ cd udpipe/src
$ make
'''

This will compile UDPipe, now put it (cp) somewhere in your $PATH, e.g. /usr/local/bin. You can find out what directories are in your $PATH by doing: echo $PATH.
Now download the UD_Finnish-TDT treebank.

'''
$ git clone https://github.com/UniversalDependencies/UD_Finnish-TDT
'''

If you go into the directory UD_Finnish-TDT, you will be able to train UDPipe with the following command:
'''
$ cat fi_tdt-ud-train.conllu | udpipe --tokenizer=none --parser=none --train fi.udpipe
'''

This will produce a model file fi.udpipe which you can then use for tagging:

'''
$ cat fi_tdt-ud-test.conllu | udpipe --tag fi.udpipe > fi_tdt-ud-test_output.conllu
'''

You can use the CoNLL-2017 evaluation script to evaluate the tagger performance:

'''
$ python3 conll17_ud_eval.py --verbose fi_tdt-ud-test.conllu fi_tdt-ud-test_output.conllu
'''
Output - 

'''
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.63 |     94.63 |     94.63 |     94.63
XPOS       |     95.77 |     95.77 |     95.77 |     95.77
Feats      |     90.86 |     90.86 |     90.86 |     90.86
AllTags    |     89.82 |     89.82 |     89.82 |     89.82
Lemmas     |     84.86 |     84.86 |     84.86 |     84.86
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
'''

Using a (very) simple perceptron tagger for CoNLL-U files - 

Perceptron tagger uses supervised machine learning to tackle the POS problem. We can see that with defualt values the accuracy of the perceptron is less than UDPipe but if we can tweak the features, we can achieve better accuracy.

Steps followed - 

The objective of this task is to download and run a very basic averaged perceptron tagger (less than 300 lines of Python).

First download the code:

'''
$ git clone https://github.com/ftyers/conllu-perceptron-tagger.git
'''

Then download some data, feel free to replace UD_Finnish with any language in UD.

'''
$ git clone https://github.com/UniversalDependencies/UD_Finnish-TDT
''''

Then download the CoNLL shared task 2017 official evaluation script and unzip it:

'''
$ wget http://universaldependencies.org/conll17/eval.zip
$ unzip eval.zip
'''

Finally enter the directory of the perceptron tagger:

'''
$ cd conllu-perceptron-tagger
'''

You can train the tagger using the following command:
 '''
 cat ../fi_tdt-ud-train.conllu | python3 tagger.py -t fi-ud.dat
 '''
 Output - 
 '''
 163223
Iter 0: 131852/163223=80.78028219062264
163217
Iter 1: 145060/163223=88.87227902930347
163216
Iter 2: 151975/163223=93.10881432151106
163213
Iter 3: 155938/163223=95.53678096836843
163220
Iter 4: 157950/163223=96.76945038383072
'''
Now you can run the tagger

'''
$  cat ../fi_tdt-ud-test.conllu | python3 tagger.py fi-ud.dat > fi-ud-test.out
'''

And evaluate:
'''
$ python3 ../conll17_ud_eval.py --verbose ../fi_tdt-ud-test.conllu fi-ud-test.out
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.40 |     90.40 |     90.40 |     90.40
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.40 |     90.40 |     90.40 |     90.40
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
'''
#Comparative Study - 
UDPipe performs better versus the default perceptron based tagger.
UDPipe provides language-agnostic tokenization, tagging, lemmatization and dependency parsing of raw text, which is an essential part in natural language processing.
UDPipe allows to work with data in CONLL-U format .
Perceptron tagger uses supervised machine learning to tackle the POS problem. We can see that with defualt values the accuracy of the perceptron is less than UDPipe but if we tweak the features, we can achieve better accuracy.

By updating tagger.py to add 3 more features - 
'''
# New features
        add('i pref2', word[:1])
        add('i pref3', word[:2])
        add('i pref4', word[:3])
'''
We can see improvement in the UPOS - 
'''
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     91.52 |     91.52 |     91.52 |     91.52
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     91.52 |     91.52 |     91.52 |     91.52
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
'''
