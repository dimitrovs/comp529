import os
import re

src_location = '../angular.js/src/'

module_regex = re.compile(r'.*\.js')

total_num_modules = 0

for root, subFolders, files in os.walk(src_location):
    for file_name in files:
        if module_regex.match(file_name):
            total_num_modules += 1

print 'Modules: '+str(total_num_modules)
