#Converts xml files to txt

import os
import datetime


[os.rename(f, f.replace('.xml', '.txt')) for f in os.listdir('.') if not f.startswith('.')]

#Clears the temp file
open('temp.txt', 'w')
open('temp.txt', 'w').close()

#Opens the files and pulls out the monthly rolling history, writing it to temp.txt

count = 1
for filename in os.listdir(os.getcwd()):
        total = len(os.listdir(os.getcwd()))
        print('Progress: Extraction ' + str(count) + ' of ' + str(total) + ' (@' + str(datetime.datetime.now().time()) + ')')
        for line in open(filename, encoding='utf8'):
                if line[:8] == ' <Return':
                        if line[41:43] != line[62:64]:
                                open('temp.txt', 'a').write(filename[0:8] + '\t' + line[19:22] + '\t' + line[35:45] + '\t' + line[56:66] + '\n')
                                open(filename, encoding='utf8').close()
                                open('temp.txt', 'a').close()
        count = count + 1

#Gap hunting on basis of temp file and outputting to output.txt

open('output.txt', 'w')
open('output.txt', 'w').close()

count2 = 1
for line in open('temp.txt', 'r'):
        num_lines = sum(1 for line in open('temp.txt', 'r'))
        print('Progress: Sorting ' + str(count2) + ' of ' + str(num_lines) + ' (@' + str(datetime.datetime.now().time()) + ')')
        if count2 == 1:
                count2 = count2 + 1
                previd = line[:8]
                prevcurr = line[9:12]
                prevend = line[24:34]
                continue
        else:
                currentid = line[:8]
                currentcurr = line[9:12]
                currentstart = line[13:23]
                if (currentid == previd) and (currentcurr == prevcurr) and (currentstart != prevend):
                        open('output.txt', 'a').write(currentid + '\t' + currentcurr + '\t' + prevend + '\t' + currentstart + '\n')
                previd = currentid
                prevcurr = currentcurr
                prevend = line[24:34]
                count2 = count2 + 1
open('temp.txt', 'r').close()
open('output.txt', 'a').close()
print('That\'s all folks!')
        
