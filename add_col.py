#!/usr/bin/python3

# add_col.py : add a time column to csv file
# usage: python add_col.py <input_file> [-o <output_file>]

import argparse

TIME_INTERVAL = 0.002

parser = argparse.ArgumentParser(description='Add a time column to csv file')
parser.add_argument('input_file', metavar='input_file', type=str, nargs=1)
parser.add_argument('-o', '--output_file', metavar='output_file', type=str, nargs=1)

args = parser.parse_args()

input_file = args.input_file[0]
output_file = args.output_file[0] if args.output_file else input_file[:-4] + '_time.csv'

print('input_file: %s' % input_file)
print('output_file: %s' % output_file)

file = open(input_file, 'r')
cnt = 0
with open(output_file, 'w') as f:
    for line in file:
        f.write('{:.3f} {}'.format(cnt * TIME_INTERVAL, line))
        cnt += 1
