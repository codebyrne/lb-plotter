#! /usr/bin/python3

import os
from matplotlib import pyplot as plt
from numpy import mean, pi
from time import sleep

def generateArray(filename):
    # Get the data from a file
    
    data_array = []
    
    try:
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                for line in f.readlines():
                    data_array.append(float(line.strip()))                

    except Exception as e:
        print("Error reading file: %s" % str(e))

    return data_array


def plotData(x_values, y_values, title = "Title", x_label = "", y_label = "", y_min = 0, y_max = 0):

    # Format matplotlib
    plt.rcParams['axes.facecolor'] = '000000'
    plt.rcParams['figure.facecolor'] = '202020'
    plt.rcParams['grid.linestyle'] = ':'
    plt.rcParams['grid.color'] = 'D3D3D3'
    plt.rcParams['text.color'] = 'FFFFFF'
    plt.rcParams['axes.labelcolor'] = 'FFFFFF'
    plt.rcParams['xtick.color'] = 'FFFFFF'
    plt.rcParams['ytick.color'] = 'FFFFFF'

    if not ((y_min == 0) and (y_max == 0)):
        ax = plt.gca()
        ax.set_ylim(y_min, y_max)

    # Plot the Data
    plt.plot(x_values, y_values, color='#FFFF00')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()

    # Static Plot
    plt.show()

    # Animate the plot.
    # plt.draw()
    # plt.pause(0.00001)
    # plt.clf()


if __name__ == "__main__":
    if len(os.sys.argv) == 7:
        filename_param = os.sys.argv[1]
        title_param = os.sys.argv[2]
        x_label_param = os.sys.argv[3]
        y_label_param = os.sys.argv[4]
        y_min_param = float(os.sys.argv[5])
        y_max_param = float(os.sys.argv[6])
    else:
        print("Usage: %s <filename> <title> <x-label> <y-label> <y-min> <y-max>" % os.sys.argv[0])
        os.sys.exit(0)

    y_array = generateArray(filename_param)
    x_array = [i for i in range(0, len(y_array))]
    plotData(x_array, y_array, title=title_param, x_label=x_label_param, y_label=y_label_param, y_min=y_min_param, y_max=y_max_param)