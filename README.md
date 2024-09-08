# 📝 Simple POS Tagging using NLTK

 This project demonstrates how to perform Part-of-Speech (POS) tagging using the NLTK (Natural Language Toolkit) library in Python. You can input any sentence, and the program will tokenize it and tag each word with its respective part of speech!

 ### 📋 Features

 - Takes a sentence as input.
 - Tokenizes the sentence into individual words.
 - Tags each word with its corresponding Part of Speech (POS).
 - Provides an easy-to-understand example of how to use NLTK's word_tokenize and pos_tag functions.

 ### 🚀 How to Run

 Follow these simple steps to get the program up and running!

 #### 1. Clone the Repository

 First, clone the repository to your local machine:


    https://github.com/Amit72777/NLP-Assignment.git


 #### 2. Install NLTK:
   Make sure you have NLTK installed. If not, install it using pip:
  
    pip install nltk
    

 #### 3. Run the script:
  You can run the code directly from your terminal or IDE:
```
    Part-of-speedTagging.py
```

 ### 🚀 How to Use

 - After running the script, the program will prompt you to enter a sentence.
 - The script will tokenize the sentence and provide the *POS tags* for each word.

 #### Example:

     Enter the sentence: The quick brown fox jumps over the lazy dog.

 #### Output:

 ```Copy code
The - DT
quick - JJ
brown - NN
fox - NN
jumps - VBZ
over - IN
the - DT
lazy - JJ
dog - NN

 ```

 ### 🧐 Code Breakdown:

 - nltk.download('punkt') and nltk.download('averaged_perceptron_tagger'): Download the necessary tokenizers and taggers from NLTK
 - word_tokenize(sentence): This tokenizes the input sentence into individual words.
 -  nltk.pos_tag(tokens): This function tags each token with its corresponding Part-of-Speech.
 -   The for loop: Iterates over the tagged sentence and prints each word with its POS tag.


 ### 🏁 Conclusion
 This project provides a simple and effective way to perform POS tagging using Python's NLTK library.
 It's a great tool for basic natural language processing (NLP) tasks. Feel free to modify and expand upon the project to suit your needs!



# 🤖 Simple Chatbot with NLTK

This project is a basic chatbot built using the *NLTK* library. The bot can recognize patterns in user input and respond with pre-defined responses. It's a simple yet interesting implementation to show how chatbots work using *regular expressions* and *reflection pairs*.

### ✨ Features

- Recognizes basic greetings and responds accordingly.
- Can engage in a simple conversation with predefined patterns.
- Provides fun answers to silly questions like "Will you kill humans?" 😄
- Allows you to exit the chat anytime by typing "quit".
  
### Instructions:

1. Clone this repository or download the code files.
2. Install NLTK: pip install nltk
3. Open a Python terminal or IDE.
4. Navigate to the directory containing the chatbot code file (e.g., chatbot.py). 
5. Run the script: python bot.py 🐍
6. Start interacting with the chatbot by typing your messages and pressing Enter.
7.   Apologies:  Responds to apologies with "It's alright" or "It's OK, never mind".
8.   Exit: Allows users to quit the conversation using "quit".


 ### 🛠 Installation

 To get started, you'll need to install the nltk library if you haven't already:

    pip install nltk

 ### Disclaimer: 

  While this code is intended for educational purposes, be cautious when building chatbots that interact with real users. It's essential to consider ethical implications and potential biases in the training data.

 ### 💡 Conclusion 

 This chatbot is a basic implementation but can easily be extended with more patterns and responses. It's a great starting point for learning about chatbots and natural language processing! 🎉
