import os
import re

src_location = '../angular.js/src/'

functions_regex = re.compile(r'function.*{')

total_num_functions = 0

for root, subFolders, files in os.walk(src_location):
    for file_name in files:
        with open(os.path.join(root, file_name), 'r') as fin:
            for line in fin:
                total_num_functions += len(functions_regex.findall(line))

print 'Functions: '+str(total_num_functions)
