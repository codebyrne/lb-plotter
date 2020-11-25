#! /usr/bin/python3

import os
from matplotlib import pyplot as plt
from numpy import mean, pi
from time import sleep

def read_yarray_from_file(filename):
    # Get the y series data from a file
    
    data_array = []
    
    try:
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                for line in f.readlines():
                    data_array.append(float(line.strip()))                

    except Exception as e:
        print("Error reading file: %s" % str(e))

    return data_array

def plot_data(x_values, y_values, title = "Title", x_label = "", y_label = "", y_min = 0, y_max = 0):

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

def make_xarray(y_value_array):
    '''
    Return an array of sequential x values for each y value.
    '''

    return [i for i in range(0, len(y_value_array))]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="A file of float values in a column")
    parser.add_argument("--title", help="The title for the plot")
    parser.add_argument("--xlabel", help="The label for the x axis")
    parser.add_argument("--ylabel", help="The label for the y axis")
    parser.add_argument("--ymin", help="The y axis min value", type=float, default=0.0)
    parser.add_argument("--ymax", help="The y axis max value", type=float, default=0.0)

    args = parser.parse_args()

    y_array = read_yarray_from_file(args.filename)
    x_array = make_xarray(y_array)
    plot_data(x_array, y_array, title=args.title, x_label=args.xlabel, y_label=args.ylabel, y_min=args.ymin, y_max=args.ymax)
