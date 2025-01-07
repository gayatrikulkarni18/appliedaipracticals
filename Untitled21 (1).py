#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
nltk.download('brown')
from nltk.corpus import brown


# In[6]:


sent=brown.sents()
tag_sent=brown.tagged_sents()
print('Sentences in browncorpus', sent[0])
print('Tagged senten ',tag_sent[0])
print('Total sentences in brown corpus',len(sent))
'''print('categories in brown',brown.categories())
print('words in brown',brown.words())
print('fiction category',brown.raw(categories='fiction'))'''


# In[9]:


sent=brown.sents()
tag_sent=brown.tagged_sents()
print('Sentences in browncorpus', sent[0])
print('Tagged senten ',tag_sent[0])
print('Total sentences in brown corpus',len(sent))
print('categories in brown',brown.categories())
print('words in brown',brown.words())
print('fiction category',brown.raw(categories='fiction'))


# In[10]:


sent=brown.sents()
tag_sent=brown.tagged_sents()
print('Sentences in browncorpus', sent[0])
print('Tagged senten ',tag_sent[0])
print('Total sentences in brown corpus',len(sent))
print('categories in brown',brown.categories())
print('words in brown',brown.words())
#print('fiction category',brown.raw(categories='fiction'))


# In[12]:


txt="Hi This is Gayatri Kulkarni"
print(txt)
print(type(txt))

for w in txt:
    print(w)


# In[13]:


txt="Hi This is Gayatri Kulkarni"
wlst=txt.split()
print(wlst)
print(type(txt))

for w in wlst:
    print(w)


# In[14]:


import pandas as pd
df=pd.read_txt('gayatri.txt')
df.head()


# In[18]:


import os
import pandas as pd
file_path = 'gayatri.txt'
data = pd.read_csv(file_path, delimiter = "\t")

data


# In[ ]:


try:
    data = pd.read_csv(file_path, delimiter="\t")
except FileNotFoundError:
    print("File not found. Please check the file path.")


# In[23]:


import pandas as pd
df=pd.read_csv(r 'gayatri.txt')
print(df['txt'])
print(df['sentiments'])


# In[26]:


txt="Hi This is Gayatri Kulkarni.I am student of MSCIT"
wlst=txt.split('.')
print(wlst)
print(type(txt))

for w in wlst:
    print(w)


# In[29]:


txt="Hi This is Gayatri Kulkarni.I am student of MSCIT"
wlst=txt.split()
print(wlst)
print(type(txt))

for w in wlst:
    print(w)
    
stwd=['is','a', 'am']
nostwd=[]
for w in wlst:
    if w not in stwd:
        nostwd.append(w)
        print('without stop words',w)


# In[31]:


txt="Hi This is Gayatri Kulkarni.I am student of MSCIT"
wlst=txt.split()
print(wlst)
print(type(txt))

for w in wlst:
    print(w)
    
stwd=['is','a', 'am']
nostwd=[]
nostwd=[w for w in wlst if w not in stwd]
print(stwd)
''''for w in wlst:
    if w not in stwd:
        nostwd.append(w)
        print('without stop words',w)'''
from nltk.tokenize import word_tokeinzation


# In[ ]:


nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = "This this is NLP work demonstarting to remove stop words"
stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
custom_stopwords.update{'is','a','am'}
stop_words.update(custom_stopwords)
filtered_words = [word for word in words]

