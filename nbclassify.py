import sys
import os
import math

root_dir = ''
ham_files = 0
spam_files = 0
ham_predicted = 0
spam_predicted = 0
msg_ham_prob = 0.0
msg_spam_prob = 0.0
ham_flag = False
spam_flag = False

dev_dir = sys.argv[1:]

d = {}
d1 = {}

for entry in dev_dir:
    root_dir += entry

f = open("nbmodel.txt", "r", encoding="latin1")
data = f.read().splitlines()
for i, record in enumerate(data):
    content = record.split()
    if i > 2:
        d[content[0]] = [float(content[1]), float(content[2])]
    elif i == 0:
        vocabulary_size = int(content[2])
    elif i == 1:
        spam_probability = float(content[1])
    elif i == 2:
        ham_probability = float(content[1])
f.close()

f1 = open("nboutput.txt", "w", encoding="latin1")

for root, sub, files in os.walk(root_dir):
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

                #  Message spam probability

                for token in token_list:
                    if token in d.keys() and d[token][0] != 0.0:
                        msg_ham_prob += d[token][0]
                    # if d[token][0] == 0.0:
                    #     continue

                #  Message spam probability
                for token in token_list:
                    if token in d.keys() and d[token][1] != 0.0:
                        msg_spam_prob += d[token][1]

                if ham_flag:
                    ham_files += 1
                if spam_flag:
                    spam_files += 1
                file_ptr.close()
                # denominator = math.log(ham_probability) + msg_ham_prob + math.log(spam_probability) + msg_spam_prob
                h = ham_probability + msg_ham_prob
                s = spam_probability + msg_spam_prob
                if h > s:
                    str1 = "ham " + str(os.path.join(root, name))
                    f1.write(str1 + "\n")
                    if ham_flag:
                        ham_predicted += 1

                elif h < s:
                    str1 = "spam " + str(os.path.join(root, name))
                    f1.write(str1 + "\n")
                    if spam_flag:
                        spam_predicted += 1
                else:
                    str1 = "spam " + str(os.path.join(root, name))
                    f1.write(str1 + "\n")
f1.close()
if ham_files != 0:
    ham_accuracy = ham_predicted/ham_files
if spam_files != 0:
    spam_accuracy = spam_predicted/spam_files
# print(ham_accuracy,spam_accuracy)
