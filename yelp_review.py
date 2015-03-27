# -*- coding: utf-8 -*-
import nltk
import re
import string
import os
#import jsonify
os.chdir("C:\Python34")
score_dict={}
#dictionary for scores
so=open("scores.txt","r")
for lin in so:
    score_dict[lin[:lin.index('\t')]]=lin[lin.index("\t")+1:-1]



    
#read file and make a dictionary
f=open("review.txt","r")
fr=f.readlines()
lis_dict=[]
for line in fr:
    #print(line)
#read it in and use eval to convert each line to a dictionary
    fd=eval(line)
    #then append it to a list
    #print(fd)
    lis_dict.append(fd)
    #print(lis_dict)

f.close()

string_dict=[]
i=0
dict1={}
for d in lis_dict:
   # print(d["text"])
    #if 'text' in d:
    if string_dict.__contains__(d['business_id']):
        #string_dict.append({d['business_id']:d['text']})
        dict1[d['business_id']] = d['text']
    else:
        dict1[d['business_id']] = d['text']

        #string_dict.append({d['business_id']:d['text']})


#print(string_dict)
def text_parse(t):
  #  print('\n\n\nfunctionnnnnnnnnnnnnnnnnnnnnnn\n')
    t=t.lower()
    t=re.sub('[^a-zA-Z]',' ',t)#anything that doesnt begin with an alphabet is removed
    for i in codelist:
        stopstring=' '+i+' '
        t=re.sub(stopstring,' ',t)#stop words are removed
    for i in stoplist:
        stopstring=' '+i+' '
        t=re.sub(stopstring,' ',t)
    t=re.sub('\s.\s',' ',t)#single letter words removed
    t=re.sub('\s',' ',t)#multiple spaces replaced with single space
    t=t.strip()
    return t

#print('\n\n\nenddddddddddddddddddddddddddddddd\n')
f=open("final.txt","w")


for key,value in dict1.items():
  #  print(key)
   # f.write(key)
    #f.write('\t')
    t=''.join(value)
    p=string.punctuation
    d=string.digits
    table=str.maketrans(p,' '*len(p))#remove punctuation
    t=value.translate(table)
    table=str.maketrans(d,' '*len(d))#remove digits
    t=t.translate(table)
    
    
   # print('\n\n\n$$$$$$$$$$$$$$$$$$$$$\n')
#create a list of stop words and stop lists
    codelist=['/r','/n','/t']
    more_stop_words=['cant','didnt','doesnt','dont','goes','isnt','hes',\
    'shes','thats','theres','theyre','wont','youll','youre','youve',\
    're','tv','g','us','en','ve','vg','didn','pg','gp','our','we',
    'll','film','video','name','years','days','one','two','three',\
    'four','five','six','seven','eight','nine','ten','eleven','twelve','http','rt','co','amp'] 



    stoplist=nltk.corpus.stopwords.words('english')+more_stop_words
    t=text_parse(t)#call parse function   
    print(t)
    
 
   