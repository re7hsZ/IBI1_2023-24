import regex # Import regex to solve the problem where the re cannot find fields that match the expression in overlapping areas
seq = "ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
n = regex.findall('GTGTGT|GTCTGT', seq, overlapped = True) # add overlapped to search overlapping areas
print(len(n))