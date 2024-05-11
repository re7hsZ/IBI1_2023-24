# input the repetitive sequence
repetitive_seq = input("Plsase input ‘GTGTGT’ or ‘GTCTGT’.\n")
# open the folder contains the file
import os
os.chdir("/Users/zhuqin/Desktop/academic/IBI/Practical 8")
# open input and output files
import re
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
if repetitive_seq == 'GTGTGT':
    output_file = open('GTGTGT_duplicate_genes.fa','w')
if repetitive_seq == 'GTCTGT':
    output_file = open('GTCTGT_duplicate_genes.fa','w')
seq = ''
i = 0
name = []
import regex # Import regex to solve the problem where the re cannot find fields that match the expression in overlapping areas
for line in input_file:
    if line.startswith(">"):
        name.append(str(re.findall(r'gene:(.+)\sgene_biotype', line))) # see if it matches the regular expression
        n = regex.findall(repetitive_seq, seq, overlapped = True) # add overlapped to search overlapping areas
        count = len(n)
        if count != 0: # if have the repetitive sequence
            name[i-1] = name[i-1] + ' ' + str(count) + '\n' + seq + '\n'
            output_file.write(name[i-1]) # write
        i += 1
        seq = ''
    else:
        seq += re.sub(r'\n','', line) # stroe the whole sequence without '\n' in the string