Assignment 3. Due: Thurs Sept 23, 11:59pm 70 points total.

This assignment is written in a lab format, with a number of tasks to provide you with exposure to NLTK and natural language processing. 

In order to complete this lab, you will need NLTK (https://www.nltk.org/) (it’s in conda, if you use that).

We’ll be reading from the NLTK book, which can be found here: https://www.nltk.org/book/ 

To submit: add code and documents to your GitHub repo for this assignment, along with documentation 
sufficient to figure out how to run your code. 

1.  (5 points) Please read chapter 1, sections 1 and 3. Please feel free to skim the parts about Python as necessary. 
Choose one of the intro texts and compute its lexical diversity.

2. (5 points) Generate the bigrams for this text.

3. (10 points) Generate a FreqDist for this text to identify the 50 most common words. 
Filter the text to lower case, remove non-words and stopwords to see if you can generate a more informative distribution.

4. (10 points) Please read chapter 2, sections 1 and 2. 
Choose one of the Gutenberg texts and create a FreqDict with it as you did above.  
Be sure to remove stop words, convert to lower case and remove non-words.

5. (10 points) Next, create a ConditionalFreqDist (CFD), where the conditions are the fileids in the Gutenberg corpus and 
the events are the words in Gutenberg.words(), filtered as above to convert to lower case, and 
remove stop words and non-words.

6. (10 points) Write a program that computes the document frequency for each word in your CFD.  

7. (10 points) Use this to generate a TFIDF score for each word in your CFD. For each document, you should 
have a dict that maps words to TFIDF scores. You might want to store these in a dict() as the CFD does.

8. (10 points) Write a function to compute cosine similarity. It should take as input two of the 
TFIDF dicts you created in the previous step and return a value between 0.0 and 1.0. 
Try it out on the different texts - are there any surprises?

