import nltk # import library 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

def pos_tagging(sentence):
  tokens = word_tokenize(sentence)
  tags = nltk.pos_tag(tokens)
  return tags
#input text
sentence = input("Enter the sentence:  ")
tagged_sentence = pos_tagging(sentence)

#print the text 
for word, tag in tagged_sentence:
        print(f"{word} - {tag}")
