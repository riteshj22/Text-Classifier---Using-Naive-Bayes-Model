# Text-Classifier---Using-Naive-Bayes-Model
A text classifier for spam filtering with training data that is pre - tokenized.

Classification technique: 
  Naive Bayes model
  
    - This model uses  the probability to classify if a particular email is ham or spam. Requires tokenized emails to create a model for classification. It builds a vocabulary of the distinct words from email data and calculates their respective ham and spam probabilities. Dump the data in the model file to be used later to classift random data.

Dataset required:

For nblearn.py:

  Tokenized data  files of emails pre classified as ham ( valid ) and spam ( invalid ) emails in their respective folders i.e "ham" or "spam"      in lowercase.

For nbclassify.py:

  Tokenized data files from emails.


Instructions  to Run: 

Step 1) 
  Objective: Creating a classification model to be used as a reference for future use by learning from the tokenized dataset. 

  Program file: nblearn.py

  Input: It takes command line input that is a directory path to tokenized data 
  For eg) C:\Users\XYX\Desktop\data_folder
  
  Output: Model file
  
          You can find the sample model file generated previously for a dataset named as nbmodel.txt
          

Step 2)

  Objective: Classifying the random data using the model file generated in step 1. 

  Program file: nbclassify.py

  Input:  1)  nbmodel.txt file 
          2)  Random tokenized data file.
  
  Output:  the efficiency of the program 
          for eg) 99/100

 
