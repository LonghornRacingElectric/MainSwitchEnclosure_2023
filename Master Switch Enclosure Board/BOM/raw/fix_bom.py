import csv
import sys

input_file = sys.argv[1]
output_file = input_file[:-4] + " - fixed.csv"

input_csv = open(input_file, newline='')
output_csv = open(output_file, 'w', newline='')

csv_reader = csv.reader(input_csv, delimiter=";", quotechar='"')
csv_writer = csv.writer(output_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

csv_writer.writerows(csv_reader)

input_csv.close()
output_csv.close()
