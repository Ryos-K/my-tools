#!/usr/bin/python3

# csv_avg.py : average csv files
# usage      : python csv_avg.py <input_files> [-o <output_file>]

import csv
import argparse

parser = argparse.ArgumentParser(description="Average csv files")
parser.add_argument("input_files", metavar="input_files", type=str, nargs="+")
parser.add_argument("-o", "--output_file", metavar="output_file", type=str, nargs=1)

args = parser.parse_args()

input_files = args.input_files
output_file = args.output_file[0] if args.output_file else "output.csv"

print("input_files: %s" % input_files)
print("output_file: %s" % output_file)

data_list = []

for input_file in input_files:
    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)

        data_list.append(data)

data_avg = []
row_count = len(data_list[0])
col_count = len(data_list[0][0])

for i in range(row_count):
    data_avg.append([0.0] * col_count)

for ri in range(row_count):
    for ci in range(col_count):
        for di in range(len(data_list)):
            data_avg[ri][ci] += float(data_list[di][ri][ci])
        data_avg[i][j] /= len(data_list)

with open(output_file, "w") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(data_avg)
