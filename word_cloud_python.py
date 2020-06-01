#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# This script processes the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# <br><br>
# **Enabling notebook extension fileupload/extension...**
# <br>


# In[1]:

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# In[2]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# <br><br>


# In[13]:


def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    frequencies ={}
    file_contents=file_contents.split()
    str1=""
    
    for word in file_contents:
        str1=''.join(ch for ch in word if ch.isalnum())
        if str1.lower() not in uninteresting_words:
            
            if str1.lower() not in frequencies:
                frequencies[str1.lower()]=1
            else:
                frequencies[str1.lower()]+=1
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# In[14]:


# Display the wordcloud image

myimage = calculate_frequencies(file_contents)                                                                                                                                                                                                                                                                                          
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

