# Pseudocode:
# Change the current working directory to where the FASTA file is stored
# Open the input FASTA file for reading and prepare to open an output file
# Initialize variables to store sequence data and gene names
# Loop through each line in the input file
#   If the line starts with ">", it's a new gene, so process the previous gene's sequence
#   Check if the description contains the word 'duplication'
#   Write the gene information and sequence to the output file if it contains 'duplication'
# After processing all genes, close the input and output files

# Import necessary libraries
import os
import re

# Change the current working directory to where the file is located
os.chdir("C:\Users\lenovo\Desktop\IBI\IBI1_2023-24\IBI1_2023-24\Practical8")

# Open the input FASTA file for reading and the output file for writing
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open('duplicate_genes.fa', 'w')

# Initialize variables to store sequence data and gene names
seq = ''
gene_name = []
i = 0
flag = 0

# Loop through each line in the input file
for line in input_file:
    if line.startswith(">"):
        # Check if the current gene's sequence has been written to the output file
        if flag == 1:
            # Write the first gene's information and sequence to the output file
            output_file.write(name[0] + '\n' + seq + '\n')
            flag = 0
        
        # Extract the gene name and check if 'duplication' is in the description
        description = line.strip().split()[1]
        if 'duplication' in description:
            # Write the gene's information and sequence to the output file
            gene_name = re.findall(r'gene:(.+)\sgene_biotype', line)[0]
            output_file.write(gene_name + '\n' + seq + '\n')
        
        # Reset the sequence string for the next gene and increment the gene counter
        seq = ''
        i += 1
        flag = 1  # Set the flag to indicate that a gene has been processed
    else:
        # Store the sequence data, removing newline characters
        seq += re.sub(r'\n', '', line)

# Close the input and output files
input_file.close()
output_file.close()
