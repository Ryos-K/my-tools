#!/usr/bin/python3

# plot_q.py : plot csv file
# usage     : python plot_q.py <input_files> -l legends [-o <output_file>]
# input_file: <input_file> is a csv file
# output_file: <output_file> is a png file

import csv
import argparse
import matplotlib.pyplot as plt
import numpy as np
import math

XLABEL = "episodes"
YLABELS = [
    "Q(left, turn left)",
    "Q(left, turn left)",
    "Q(left, turn around)",
    "Q(right, turn left)",
    "Q(right, turn right)",
    "Q(right, turn around)",
    "Q(backward, turn left)",
    "Q(backward, turn right)",
    "Q(backward, turn around)",
]
LINESTYLES = ["-", "--", "-.", ":"]

parser = argparse.ArgumentParser(description="Plot csv file")
parser.add_argument("input_files", metavar="input_files", type=str, nargs="+")
parser.add_argument("-l", "--legends", metavar="legends", type=str, nargs="+")
parser.add_argument("-o", "--output_file", metavar="output_file", type=str, nargs=1)

args = parser.parse_args()

input_files = args.input_files
output_file = args.output_file[0] if args.output_file else "output.png"
legends = args.legends if args.legends else None

if len(input_files) != len(legends):
    print("input_files and legends must be the same length")
    exit(1)

if len(input_files) > len(LINESTYLES):
    print("input_files must be less than %d" % len(LINESTYLES))
    exit(1)

print("input_files: %s" % input_files)
print("output_file: %s" % output_file)

q_list = []

for input_file in input_files:
    with open(input_file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        data = list(reader)

        q11 = [float(row[0]) for row in data]
        q12 = [float(row[1]) for row in data]
        q13 = [float(row[2]) for row in data]
        q21 = [float(row[3]) for row in data]
        q22 = [float(row[4]) for row in data]
        q23 = [float(row[5]) for row in data]
        q31 = [float(row[6]) for row in data]
        q32 = [float(row[7]) for row in data]
        q33 = [float(row[8]) for row in data]

        q_list.append([q11, q12, q13, q21, q22, q23, q31, q32, q33])

fig = plt.figure(figsize=(12, 10))

x = np.linspace(0, len(q_list[0][0]), len(q_list[0][0]))

for i in range(9):
    ax = fig.add_subplot(3, 3, i + 1)

    for j in range(len(input_files)):
        if legends:
            ax.plot(x, q_list[j][i], label=legends[j], linestyle=LINESTYLES[j])
        else:
            ax.plot(x, q_list[j][i])

    ax.set_ylim([-1.1, 1.1])
    ax.set_xlabel(XLABEL)
    ax.set_ylabel(YLABELS[i])
    if legends:
        ax.legend()

plt.tight_layout()
plt.savefig(output_file)
plt.show()
