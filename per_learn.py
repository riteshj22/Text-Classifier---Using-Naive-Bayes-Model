import math
import sys
import os

dir_path = sys.argv[1]

# Dictionary to store distinct words from training dataset.

vocabulary = {}

# To maintain the total number of words in Ham and Spam files respectively.

ham_total = 0
spam_total = 0

# Total number of Ham and Spam files.

ham_files = 0
spam_files = 0

# For probabilities of Spam and Ham

spam = 0.0
ham = 0.0


# **********************************************************************************************************************
#   Each key in Vocabulary Dictionary has a list of size 4 as it's value
#   1st element of list i.e list[0] stores the frequency of the word in Ham files
#   2nd element of list i.e list[1] stores the frequency of the word in Spam files
#   3rd element of list i.e list[2] stores the probability of the word in Ham files
#   3rd element of list i.e list[2] stores the probability of the word in Ham files
# **********************************************************************************************************************

# ******************************************** Traversing the given directory *****************************************#

for root, sub, files in os.walk(dir_path):

    if "/" in root:
        parent = root.split("/")
    elif "\\" in root:
        parent = root.split("\\")
    parent = parent[-1]
    if parent.lower() == "ham":
        for name in files:
            ham_files += 1
            if name.endswith(".txt"):
                file_ptr = open(os.path.join(root, name), "r", encoding="latin1")
                token_list = file_ptr.read().split()
                for token in token_list:
                    # if token.isalnum():
                    if token not in vocabulary.keys():
                        # if token.lower() not in stop_words:
                        # ham_dir[token] = [1, 0]
                        vocabulary[token] = [1, 0, 0, 0]
                        ham_total += 1
                        # ham_count += 1
                    else:
                        # ham_dir[token][0] += 1
                        vocabulary[token][0] += 1
                        ham_total += 1
                        # ham_count += 1
                file_ptr.close()

    if parent.lower() == "spam":
        for name in files:
            spam_files += 1
            if name.endswith(".txt"):
                file_ptr = open(os.path.join(root, name), "r", encoding="latin1")
                token_list = file_ptr.read().split()
                for token in token_list:
                    # if token.isalnum():
                    if token not in vocabulary.keys():
                        # if token.lower() not in stop_words:
                        # spam_dir[token] = [1, 0]
                        vocabulary[token] = [0, 1, 0, 0]
                        spam_total += 1
                    else:
                        # spam_dir[token][0] += 1
                        vocabulary[token][1] += 1
                        spam_total += 1
                        # spam_count += 1
            file_ptr.close()  # ********************************* Calculating Probabilities for words, classes resp. *********************************

vocabulary_size = len(vocabulary)

# ********************************************** For words in Ham files ************************************************

for key in vocabulary:
    vocabulary[key][2] = (vocabulary[key][0] + 1) / (ham_total + vocabulary_size)
    if vocabulary[key][2] != 0.0:
        vocabulary[key][2] = math.log(vocabulary[key][2])

# ********************************************** For words in Spam files ***********************************************

for key in vocabulary:
    vocabulary[key][3] = (vocabulary[key][1] + 1) / (spam_total + vocabulary_size)
    if vocabulary[key][3] != 0.0:
        vocabulary[key][3] = math.log(vocabulary[key][3])

total_files = spam_files + ham_files

if total_files != 0:
    spam = spam_files / total_files
    spam = math.log(spam)

if total_files != 0:
    ham = ham_files / total_files
    ham = math.log(ham)

# print(spam_files, ham_files)
# print(ham_total, spam_total)

# ************************************ Creating a model file based on training data ************************************

#   Format for the  Model File
#   Token Ham_probability Spam_probability

with open('nbmodel.txt', "w", encoding="latin1") as f:
    f.write("vocabulary size " + str(len(vocabulary)) + "\n")
    f.write("spam " + str(spam) + "\n")
    f.write("ham " + str(ham) + "\n")
    for key in vocabulary:
        str1 = ''
        str1 += str(key)
        str1 += " "
        value = vocabulary[key][2]
        str1 += str(value)
        str1 += " "
        value = vocabulary[key][3]
        str1 += str(value)
        f.write(str1 + "\n")

f.close()
