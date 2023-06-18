#!/usr/bin/python3

# plot.py : plot csv file
# usage: python plot.py <input_file> [-o <output_file>] [-xbgn <x_begin>] [-xend <x_end>]

import csv
import argparse
import matplotlib.pyplot as plt
import numpy as np
import math

XLABEL = 'time (s)'
YLABELS = ['x1 (m)', 'x2 (rad)', 'x3 (m/s)', 'x4 (rad/s)', 'u (V)']
YTICKS = [0.01, 0.01, 0.1, 0.1, 1]
XLIM = [0, 20]

parser = argparse.ArgumentParser(description='Plot csv file')
parser.add_argument('input_file', metavar='input_file', type=str, nargs=1)
parser.add_argument('-o', '--output_file', metavar='output_file', type=str, nargs=1)
parser.add_argument('-xbgn', '--x_begin', metavar='x_begin', type=float, nargs=1)
parser.add_argument('-xend', '--x_end', metavar='x_end', type=float, nargs=1)

args = parser.parse_args()

input_file = args.input_file[0]
output_file = args.output_file[0] if args.output_file else input_file[:-4] + '.png'
x_begin = args.x_begin[0] if args.x_begin else XLIM[0]
x_end = args.x_end[0] if args.x_end else XLIM[1]

print('input_file: %s' % input_file)
print('output_file: %s' % output_file)

with open(input_file, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    data = list(reader)

    t = [float(row[0]) for row in data]
    u = [float(row[1]) for row in data]
    x1 = [float(row[2]) for row in data]
    x2 = [float(row[3]) for row in data]
    x3 = [float(row[4]) for row in data]
    x4 = [float(row[5]) for row in data]

    xbgn_idx = 0
    xend_idx = len(t) - 1
    for i in range(len(t)):
        if t[i] >= x_begin:
            xbgn_idx = i
            break
    for i in range(len(t)):
        if t[i] >= x_end:
            xend_idx = i
            break
    

fig = plt.figure(figsize=(8, 10))
for i in range(5):
    ax = fig.add_subplot(5, 1, i + 1)
    
    ax.plot(t[xbgn_idx:xend_idx], [x1, x2, x3, x4, u][i][xbgn_idx:xend_idx])
    ax.set_xlim([x_begin, x_end])
    ax.set_yticks(np.arange(math.floor(min([x1, x2, x3, x4, u][i][xbgn_idx:xend_idx]) / YTICKS[i]) * YTICKS[i] - YTICKS[i], math.ceil(max([x1, x2, x3, x4, u][i][xbgn_idx:xend_idx]) / YTICKS[i]) * YTICKS[i] + YTICKS[i], YTICKS[i]))
    ax.set_ylabel(YLABELS[i])

ax.set_xlabel(XLABEL)


plt.tight_layout()
plt.savefig(output_file)
plt.show()
