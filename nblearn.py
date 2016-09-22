import math
import sys
import os


root_dir = ''
dir_path = sys.argv[1:]

for entry in dir_path:
    root_dir += entry

ham_dir = {}
spam_dir = {}
dir = {}
ham_total = 0
spam_total = 0
# ham_count = 0
# spam_count = 0
ham_files = 0
spam_files = 0
spam = 0.0
ham = 0.0

for root, sub, files in os.walk(root_dir):

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
                    if token.isalnum():
                        if token not in dir.keys():
                            # ham_dir[token] = [1, 0]
                            dir[token] = [1, 0, 0, 0]
                            ham_total += 1
                            # ham_count += 1
                        else:
                            # ham_dir[token][0] += 1
                            dir[token][0] += 1
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
                    if token.isalnum():
                        if token not in dir.keys():
                            # spam_dir[token] = [1, 0]
                            dir[token] = [0, 1, 0, 0]
                            spam_total += 1
                        else:
                            # spam_dir[token][0] += 1
                            dir[token][1] += 1
                            spam_total += 1
                            # spam_count += 1
                file_ptr.close()

# Calculating Probabilities for words, classes resp.


# For words in ham data

# for key in ham_dir:
#     ham_total += ham_dir[key][0]
vocabulary_size = len(dir)
for key in dir:
    dir[key][2] = (dir[key][0] + 1) / (ham_total + vocabulary_size)
    if dir[key][2] != 0.0:
        dir[key][2] = math.log(dir[key][2])

# For words in spam data

# for key in spam_dir:
#     spam_total += spam_dir[key][0]

for key in dir:
    dir[key][3] = (dir[key][1] + 1) / (spam_total + vocabulary_size)
    if dir[key][3] != 0.0:
        dir[key][3] = math.log(dir[key][3])
total_files = spam_files + ham_files
if total_files != 0:
    spam = spam_files / total_files
    spam = math.log(spam)
if total_files != 0:
    ham = ham_files / total_files
    ham = math.log(ham)
# print(spam_files, ham_files)
# print(ham_total, spam_total)

with open('nbmodel.txt', "w", encoding="latin1") as f:
    f.write("vocabulary size " + str(len(dir)) + "\n")
    f.write("spam " + str(spam) + "\n")
    f.write("ham " + str(ham) + "\n")
    for key in dir:
        str1 = ''
        str1 += str(key)
        str1 += " "
        value = dir[key][2]
        str1 += str(value)
        str1 += " "
        value = dir[key][3]
        str1 += str(value)
        f.write(str1 + '\n')

f.close()


# print("ham word count", ham_count)
# print("spam word count", spam_count)
# print("ham files", ham_files)
# print("spam_files", spam_files)
