import csv
import re

input_file = "3V1B_Ca_SymmetryValues_InterDistances.txt"
output_file = "3V1B_Ca.csv"

# Pattern: extract 'rmsd #1/B:3@Ca to #1/A:4@Ca' and '18.918'
pattern = re.compile(r'(rmsd\s+#\S+?\s+to\s+#\S+?)</a>.*?([\d.]+)<br>')

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['RMSD Description', 'RMSD Value'])  # CSV header

    for line in infile:
        if 'href="help:user/commands/rmsd.html">rmsd</a>' in line:
            match = pattern.search(line)
            if match:
                rmsd_str = match.group(1)
                rmsd_val = match.group(2)
                writer.writerow([rmsd_str, rmsd_val])
