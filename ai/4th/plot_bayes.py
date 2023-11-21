#!/usr/bin/python3

# plot_bayes.py : plot bayes probability distribution
# usage         : python plot_bayes.py <inputs> [-o <output_file>]
# inputs        : sequence of characters: 'S' or 'F'
#               : if 'S', update probability distribution with P(theta|success) = theta
#               : if 'F', update probability distribution with P(theta|failure) = 1 - theta
# output_file   : output.png

import argparse
import matplotlib.pyplot as plt
import numpy as np

XLABEL = r"$\theta$"
YLABEL = "Probability Density"
LINESTYLES = ["-", "--", "-.", ":"]
N = 1000

get_linestyle = lambda i: LINESTYLES[i % len(LINESTYLES)]

parser = argparse.ArgumentParser(description="Plot bayes probability distribution")
parser.add_argument("inputs", metavar="inputs", type=str, nargs="+")
parser.add_argument("-o", "--output_file", metavar="output_file", type=str, nargs=1)

args = parser.parse_args()

inputs = args.inputs
output_file = args.output_file[0] if args.output_file else "output.png"

# check the number of inputs is not empty
if len(inputs) == 0:
    print("inputs must not be empty")
    exit(1)
# check inputs contains only 'S' or 'F'
for input in inputs:
    if input != "S" and input != "F":
        print("inputs must contain only 'S' or 'F'")
        exit(1)

# plot
fig, ax = plt.subplots(figsize=(12, 10))
x = np.linspace(0.0, 1.0, N)
ax.set_xlabel(XLABEL)
ax.set_ylabel(YLABEL)

# initialize probability distribution
p_success = np.linspace(0.0, 1.0, N)  # P(theta|success) = theta
p_failure = 1.0 - p_success  # P(theta|failure) = 1 - theta
p_theta = np.ones(N) / N

# update probability distribution
cnt_success = 0
cnt_failure = 0
for input in inputs:
    if input == "S":
        p_theta = p_theta * p_success
        cnt_success += 1
    else:
        p_theta = p_theta * p_failure
        cnt_failure += 1
    p_theta = p_theta / np.sum(p_theta) * N

    # plot probability distribution
    ax.plot(
        x,
        p_theta,
        label="Success={} Failure={}".format(cnt_success, cnt_failure),
        linestyle=get_linestyle(len(ax.lines)),
    )


ax.legend()

# ouput
plt.savefig(output_file)
plt.show()
