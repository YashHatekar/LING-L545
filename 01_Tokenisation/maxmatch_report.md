# Max Match implementation
```
import sys
def maxmatch(sent, dictionary):
    start = ''
    remainder = ''
    if sent == '':
        return list()
    for i in range(len(sent), 1, -1):
        start = sent[0:i]
        remainder = sent[i:]
        if start in dictionary:
            return [start] + maxmatch(remainder, dictionary)
    start = sent[0:1]
    remainder = sent[1:]
    return [start] + maxmatch(remainder, dictionary)

line = sys.stdin.readline()
dictionary_file = open(sys.argv[1], "r")
dictionary = dictionary_file.read()
dictionary_list = dictionary.split("\n")
while line != '':
    print(maxmatch(line.replace(' ',''), dictionary_list))
    line = sys.stdin.readline()
dictionary_file.close()
```
# How to use MaxMatch

Save the above code as maxmatch.py

```
$ echo 'sentence to tokenise.' | python3 maxmatch.py dictionary-file
```
or

```
$ cat file_name | python3 maxmatch.py dictionary-file
```
# Performance

MaxMatch works well, using the dictionary file it is able to accurately segmenting most of the words. It should make mistakes only when either the words are unknown because the words are missiging in the dictionary file or if there exists a combination of words to create a longer word.
I wasn't able to run the WER on the entire results due to limitation of memory overwrite on linux subsystem on WIN 11.
