import os
from bs4 import BeautifulSoup

docs_location = '../angular.js/build/docs/partials/'

total_num_lines = 0
total_num_words = 0

for root, subFolders, files in os.walk(docs_location):
    for file_name in files:
        with open(os.path.join(root, file_name), 'r') as fin:
            soup = BeautifulSoup(fin)
            text = soup.get_text()
            for line in text:
                total_num_lines += 1
                total_num_words += len(line.split())

print 'Lines: '+str(total_num_lines)
print 'Words: '+str(total_num_words)
