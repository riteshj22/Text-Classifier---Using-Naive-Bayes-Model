import sys
import os

ham_files = 0
spam_files = 0


ham_predicted = 0
spam_predicted = 0

#  To calculate the message spam and ham probability

msg_ham_prob = 0.0
msg_spam_prob = 0.0

ham_flag = False
spam_flag = False

#  Count of correctly identified documents i.e spam/ham

ham_predicted_correct = 0
spam_predicted_correct = 0


dev_dir = sys.argv[1]

# Dictionary to store distinct words from training dataset.

model = {}
d1 = {}

#  *************************************** reading the model file ******************************************************

fptr = open("nbmodel.txt", "r", encoding="latin1")
data = fptr.read().splitlines()
for i, record in enumerate(data):
    content = record.split()
    if i > 2:
        model[content[0]] = [float(content[1]), float(content[2])]
    elif i == 0:
        vocabulary_size = int(content[2])
    elif i == 1:
        spam_probability = float(content[1])
    elif i == 2:
        ham_probability = float(content[1])
fptr.close()

# ***************************************** Stop Words Filter **********************************************************
stop_words = []
stop_ptr = open("stop_words.txt", "r")
words = stop_ptr.read().splitlines()
for word in words:
    stop_words.append(word)


# *********************************** Classifying the documents as spam/ham ********************************************


f1 = open("nboutput.txt", "w", encoding="latin1")

for root, sub, files in os.walk(dev_dir):
    ham_flag = False
    spam_flag = False
    if "/" in root:
        parent = root.split("/")
    elif "\\" in root:
        parent = root.split("\\")
    parent = parent[-1]
    if parent.lower() == "ham":
        ham_flag = True
    if parent.lower() == "spam":
        spam_flag = True
    if ham_flag or spam_flag:
        for name in files:
            if name.endswith(".txt"):
                msg_ham_prob = 0.0
                msg_spam_prob = 0.0
                file_ptr = open(os.path.join(root, name), "r", encoding="latin1")
                token_list = file_ptr.read().split()

                #  Message ham probability

                for token in token_list:
                    if token.isalnum():
                        if token not in stop_words:
                            if token in model.keys() and model[token][0] != 0.0:
                                msg_ham_prob += model[token][0]

                #  Message spam probability

                for token in token_list:
                    if token.isalnum():
                        if token not in stop_words:
                            if token in model.keys() and model[token][1] != 0.0:
                                msg_spam_prob += model[token][1]

                if ham_flag:
                    ham_files += 1

                if spam_flag:
                    spam_files += 1

                file_ptr.close()

                h = ham_probability + msg_ham_prob
                s = spam_probability + msg_spam_prob

                if h > s:
                    str1 = "ham " + str(os.path.join(root, name))
                    ham_predicted += 1
                    f1.write(str1 + "\n")
                    if ham_flag:
                        ham_predicted_correct += 1

                elif h < s:
                    str1 = "spam " + str(os.path.join(root, name))
                    f1.write(str1 + "\n")
                    spam_predicted += 1
                    if spam_flag:
                        spam_predicted_correct += 1
                else:
                    str1 = "spam " + str(os.path.join(root, name))
                    f1.write(str1 + "\n")
f1.close()

if ham_files != 0:
    ham_accuracy = ham_predicted_correct/ham_files

if spam_files != 0:
    spam_accuracy = spam_predicted_correct/spam_files

# print(format(ham_accuracy, '.16f'), format(spam_accuracy, '.16f'))

# *********************************** Calculating the precision, recall and F1 score values ****************************

ham_precision = ham_predicted_correct/ham_predicted
spam_precision = spam_predicted_correct/spam_predicted

ham_recall = ham_predicted_correct/ham_files
spam_recall = spam_predicted_correct/spam_files

ham_f1 = (2*ham_precision*ham_recall)/(ham_precision+ham_recall)
spam_f1 = (2*spam_precision*spam_recall)/(spam_precision+spam_recall)


print("spam precision", format(spam_precision, '.16f'))
print("spam recall", format(spam_recall, '.16f'))
print("spam F1", format(spam_f1, '.16f'))
print("ham precision", format(ham_precision, '.16f'))
print("ham recall", format(ham_recall, '.16f'))
print("ham F1", format(ham_f1, '.16f'))

