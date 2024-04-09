# open the folder contains the file
import os
os.chdir("/Users/zhuqin/Desktop/academic/IBI/Practical 8")
# open input and output files
import re
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('duplicate_genes.fa', 'w')
import regex # Import regex to solve the problem where the re cannot find fields that match the expression in overlapping areas
seq = ''
i = 0
name = []
flag = 0
for line in input_file:
    if line.startswith(">"):
        if flag == 1: # There is a problem that if the gene is in the first, seq will be empty. So I use a flag to review the first gene.
            name[0] = name[0] + '\n' + seq + '\n'
            output_file.write(name[0]) # write
            flag = 0 
        name.append(str(re.findall(r'gene:(.+)\sgene_biotype', line))) # see if it matches the regular expression
        if re.search('duplication', line):
            if i != 0:
                name[i-1] = name[i-1] + '\n' + seq + '\n'
                output_file.write(name[i-1]) # write
            else:
                flag = 1
        i += 1
        seq = ''
    else:
        seq += re.sub(r'\n','', line) # stroe the whole sequence without '\n' in the string
