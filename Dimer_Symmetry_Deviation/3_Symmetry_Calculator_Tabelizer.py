import os
import csv
import statistics

script_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_dir, 'output.txt')

with open(output_file, 'w') as out:
    out.write('Filename\tAverage Difference\tStandard Deviation\n')

    for filepath in os.listdir(script_dir):
        if filepath.endswith('.csv'):
            full_path = os.path.join(script_dir, filepath)

            values = []
            with open(full_path, 'r', newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        val = float(row[1])
                        values.append(val)
                    except (IndexError, ValueError):
                        continue

            # Compute absolute differences for consecutive pairs (1&2, 3&4, ...)
            diffs = []
            for i in range(0, len(values) - 1, 2):
                diff = abs(values[i] - values[i+1])
                diffs.append(diff)

            if diffs:
                avg = statistics.mean(diffs)
                stddev = statistics.stdev(diffs) if len(diffs) > 1 else 0.0
            else:
                avg = stddev = 0.0

            out.write(f'{filepath}\t{avg:.6f}\t{stddev:.6f}\n')
