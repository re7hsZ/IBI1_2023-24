# Pseudocode:
# Prompt the user to input one of the two repetitive sequences ('GTGTGT' or 'GTCTGT')
# Change the current working directory to where the FASTA file is stored
# Open the input FASTA file for reading and prepare to open an output file based on the user's input
# Initialize variables to store sequence data and gene names
# Loop through each line in the input file
#   If the line starts with ">", it's a new gene, so process the previous gene's sequence
#   Check for the presence of the repetitive sequence in the current gene's sequence
#   Write the gene information and sequence to the output file if the repetitive sequence is found
# After processing all genes, close the input and output files

# Import necessary libraries
import os
import re
import regex

# Prompt the user to input the repetitive sequence
repetitive_seq = input("Please input 'GTGTGT' or 'GTCTGT':\n")

# Change the current working directory to where the file is located
os.chdir("C:\Users\lenovo\Desktop\IBI\IBI1_2023-24\IBI1_2023-24\Practical8")

# Open the input FASTA file for reading
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

# Prepare the output file name based on the user's input
if repetitive_seq == 'GTGTGT':
    output_file = open('GTGTGT_duplicate_genes.fa', 'w')
elif repetitive_seq == 'GTCTGT':
    output_file = open('GTCTGT_duplicate_genes.fa', 'w')

# Initialize variables to store sequence data and gene names
seq = ''
gene_name = []
i = 0

# Loop through each line in the input file
for line in input_file:
    if line.startswith(">"):
        # Extract the gene name and check if 'duplication' is in the description
        description = line.strip().split()[1]
        if 'duplication' in description:
            # Use regex to find the gene name
            gene_name.append(re.findall(r'gene:(.+)\sgene_biotype', line)[0])
            # Find all instances of the repetitive sequence, including overlaps
            matches = regex.findall(repetitive_seq, seq, overlapped=True)
            count = len(matches)
            # Create a new sequence name with the count of repetitive elements
            new_name = f"{gene_name[i-1]} {count}"
            # Write the gene information and sequence to the output file
            output_file.write(f">{new_name}\n")
            output_file.write(seq)
            output_file.write("\n")
        i += 1
        seq = ''  # Reset the sequence string for the next gene
    else:
        # Store the sequence data, removing newline characters
        seq += re.sub(r'\n', '', line)

# Close the input and output files
input_file.close()
output_file.close()
