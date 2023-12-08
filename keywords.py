import os
import sys

# def main():
#     #initialize keywords
#     keywords = {"and", ....}
#     #get user input for file name and directory path
#     filename, dir_path = getUserInput()
#     if not validate(filename):
#         print("Invalid File Name")
#         return 1
#         if not validateDirPath(dir_path):
#             print("Invalid Directory Path")
#             return 2
#             try:
#                 with open(os.path.join(dir_path, filename), 'r') as f:
#                     text = f.read().lower()
#                     words = text.split(' ')
#                     count = Counter(words)
#                     mostCommonWords = [word[0] for word in count.most_common(5)]
#                     print("\nMost common words are : ", mostCommonWords)
#                     print("\nKeywords found in the document are : ", findKeywords(text))

def main():
    keywords = {"and", "..."} #add more keywords here.
    filename = input("Enter the file name or directory: ").strip()

    if not os.path.isFile(filename):
        print("File", filename, "doesn't exists.")

    infile = open(filename, 'r')
    text = infile.read().split()
    count = 0
    for word in text:
        if word in keywords:
            count += 1
    print("The no of keyword in ", filename, " is ", count)
