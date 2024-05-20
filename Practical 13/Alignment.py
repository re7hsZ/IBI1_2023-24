# load the matrix
import blosum as bl
matrix = bl.BLOSUM(62)
# open the folder contains the file
import os
os.chdir("/Users/zhuqin/Desktop/academic/IBI/IBI1_2023-24/Practical 13")
# open input files
human = open('SLC6A4_HUMAN.fa', 'r')
mouse = open('SLC6A4_MOUSE.fa', 'r')
rat = open('SLC6A4_RAT.fa', 'r')
# get the sequences from the file
import re
def get(input_file):
    seq = ""
    for line in input_file:
        if line.startswith(">"):
            continue
        seq += re.sub(r'\n','', line) # stroe the whole sequence without '\n' in the string
    return list(seq)
seq_human= get(human)
seq_mouse = get(mouse)
seq_rat = get(rat)
# Compare each amino acid
def Compare(seq1, seq2):
    # use BLOSUM62 to detect sequence similarities
    score = 0
    for i in range(len(seq1)):
        score += matrix[seq1[i]][seq2[i]]
    print("BLOSUM score:", score)
    # calculate the Hamming/edit distance
    edit_distance = 0 #set initial distance as zero
    for i in range(len(seq1)): #compare each amino acid
        if seq1[i] != seq2[i]:
            edit_distance += 1 #add a score 1 if amino acids are different
    print ("percentage identity:", 100 - 100 * edit_distance / len(seq1), "%")
# print the result
print("SLC6A4_HUMAN\nSLC6A4_MOUSE")
Compare(seq_human, seq_mouse)
print("SLC6A4_HUMAN\nSLC6A4_RAT")
Compare(seq_human, seq_rat)
print("SLC6A4_MOUSE\nSLC6A4_RAT")
Compare(seq_mouse, seq_rat)
