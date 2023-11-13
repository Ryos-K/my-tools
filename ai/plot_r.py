#!/usr/bin/python3

# plot_r.py : plot csv file
# usage     : plot_r.py <input_files> -l legends [-o <output_file>]

import csv
import argparse
import matplotlib.pyplot as plt
import numpy as np
import math

XLABEL = "episodes"
YLABELS = "sum of rewards"

parser = argparse.ArgumentParser(description="Plot csv file")
parser.add_argument("input_files", metavar="input_files", type=str, nargs="+")
parser.add_argument("-l", "--legends", metavar="legends", type=str, nargs="+")
parser.add_argument("-o", "--output_file", metavar="output_file", type=str, nargs=1)

args = parser.parse_args()

input_files = args.input_files
output_file = args.output_file[0] if args.output_file else "output.png"

print("input_files: %s" % input_files)
print("output_file: %s" % output_file)

r_list = []

for input_file in input_files:
    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        data = list(reader)

        r = [float(row[1]) for row in data]

        r_list.append(r)

fig = plt.figure(figsize=(12, 10))
x = np.arange(len(r_list[0]))

ax = fig.add_subplot(1, 1, 1)
for i in range(len(r_list)):
    ax.plot(x, r_list[i], label=args.legends[i])

ax.set_xlabel(XLABEL)
ax.set_ylabel(YLABELS)
ax.legend()

plt.savefig(output_file)
plt.show()
