import sys,re
import nltk
nltk.download('punkt')
#nltk.download('wordnet')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
#from nltk.stem.wordnet import WordNetLemmatizer
#from cucco import Cucco
#cucco = Cucco()
#lemmatizer = WordNetLemmatizer()
import elotl.corpus
import elotl.nahuatl.orthography
nahuatl = elotl.corpus.load('axolotl')
normalizer_sep = elotl.nahuatl.orthography.Normalizer("sep") #inali ack
normalizer_ina = elotl.nahuatl.orthography.Normalizer("inali")
normalizer_ack = elotl.nahuatl.orthography.Normalizer("ack")

with open(sys.argv[1],'r',encoding='utf-8-sig') as text:
	page_read = text.read()
	
data_mod = ''

words = page_read.split()

if len(words)%2!=0:
	words+=' '
#Reformatting title and page numbers by adding '.' in the beginning for every 'de' and in the end of every page number
for i in range(len(words)-1):
	if re.match(r'\d',words[i]):
		continue
	if words[i]=='de':
		data_mod+=' '+'.'+words[i]
		continue
	if re.match(r'[f|F]o\..[1-9][0-9]*',words[i]):
		data_mod+=' '+words[i]+'.'
	elif re.match(r'[f|F]o\..[1-9][0-9]*',(words[i]+words[i+1])):
		data_mod+=' '+words[i]+words[i+1]+'.'
		i+=1
	elif re.match(r'[f|F]ol\..[1-9][0-9]*',words[i]):
		data_mod+=' '+words[i]+'.'
	elif re.match(r'[f|F]ol\..[1-9][0-9]*',(words[i]+words[i+1])):
		data_mod+=' '+words[i]+words[i+1]+'.'
		i+=1
	else:
		data_mod+=' '+words[i]

data = data_mod.split()
#print(data)
pts = []
pte = []
fo = []

#Finding indexes for each title start and page end
for i in range(len(data)-1):
	if re.match(r'.de',data[i].lower()):
	#if data[i]=='de':
		temp_str = ' '.join(j for j in data[i:i+6])
		if re.match(r'.de .*de.*fo.*\.',temp_str.lower()):
			continue
		elif re.match(r'.de .*fo\.',temp_str.lower()) or re.match(r'.de .*fol\.',temp_str.lower()):
			#print(temp_str)
			pts.append(i)
	if re.match(r'fo\.',data[i].lower()):
		pte.append(i)
		fo.append(data[i])
	if re.match(r'fol\.',data[i].lower()):
		pte.append(i)
		fo.append(data[i])
#print(len(pts),len(pte))
#print(pts,pte)
pt = []
pgs = pts.copy()
pge = pte.copy()
#page title extraction
while pte:
	start = pts.pop(0)
	end = pte.pop(0)
	pt.append(data[start:end])

pages = []

for i in range(len(pgs)-1):
	pages.append(data[pgs[i]:pgs[i+1]])
pages.append(data[pgs[-1]:])

#print(len(pt),len(pages))
#for i in pt:
#	print(i)
#print(len(pages))	

for i in range(len(pages)):
	pgt = ' '.join(j for j in pt[i]) #Collecting all the page titles
	pg = ' '.join(el for el in pages[i]) #Collecting all the pages
	sent = sent_tokenize(pg[len(pgt)+len(fo[i])+1:]) #Tokenizing sentences from the page
	print(pg)
	for j in sent:
		#lem_sent = lemmatizer.lemmatize(j)
		#cuco_sent = cucco.normalize(j)
		j_norm =''
		nah_normalize_sep = normalizer_sep.normalize(j) #Initiallizing sep normalizer from elotl
		nah_normalize_ina = normalizer_ina.normalize(j) #Initiallizing ina normalizer from elotl
		nah_normalize_ack = normalizer_ack.normalize(j) #Initiallizing ack normalizer from elotl
		nah_phonemes_sep = normalizer_sep.to_phones(j)
		nah_phonemes_ina = normalizer_ina.to_phones(j)
		nah_phonemes_ack = normalizer_ack.to_phones(j)
		#print('-------- Using WordNet Lemmatizer --------')
		#print(pgt,'\t',fo[i],'\t',j,'\t',lem_sent)
		#print('-------- Using Cucco --------')
		#print(pgt,'\t',fo[i],'\t',j,'\t',cuco_sent)
		print('-------- Using elotl sep--------')
		print(pgt,'\t',fo[i],'\t',j,'\t',nah_normalize_sep)
		print('-------- Using elotl ina--------')
		print(pgt,'\t',fo[i],'\t',j,'\t',nah_normalize_ina)
		print('-------- Using elotl ack--------')
		print(pgt,'\t',fo[i],'\t',j,'\t',nah_normalize_ack)
		print('-------- Using custom rules ----')
		j_temp = j.split()
		for k in j_temp:
			if 'u' in k:
				j_norm += ' '+k.replace('u','o')
			elif 'yj' in k:
				j_norm += ' '+k.replace('yj','i')
			elif 'iao' in k:
				j_norm += ' '+k.replace('iao','yao')
			elif 'ynjn' in k:
				j_norm += ' '+k.replace('ynjn','inin')
			elif 'cve' in k:
				j_norm += ' '+k.replace('cve','cue')
			elif 'vit' in k:
				j_norm += ' '+k.replace('vit','iit')
			elif 'V' in k:
				j_norm += ' '+k.replace('V', 'Hu')
			elif 'b' in k:
				j_norm += ' '+k.replace('b', 'p')
			else:
				j_norm +=' '+k
		print (pgt,'\t',fo[i],'\t',j,'\t',j_norm)
		# to generate phonemes uncomment below lines
		#print('-------- Using elotl sep phonemes--------')
		#print(pgt,'\t',fo[i],'\t',j,'\t',nah_phonemes_sep)
		#print('-------- Using elotl ina phonemes--------')
		#print(pgt,'\t',fo[i],'\t',j,'\t',nah_phonemes_ina)
		#print('-------- Using elotl ack phonemes--------')
		#print(pgt,'\t',fo[i],'\t',j,'\t',nah_phonemes_ack)
	print('-------- --------')

