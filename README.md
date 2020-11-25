# lb-plotter
Generic pyplot configuration with colors that I like (or can see anyway!)

Easily plots a one-dimensional array, with various options from which to source
the data. 

# plotter module
* The plotter module takes a file containing floats, one per line as an
argument.
  * Usage: 
  ## plot_data()
    * Plots the data given an x and y array.
  ## read_yarray_from_file()
    * Get the y series data from a file
  ## make_xarray()
    * Return an array of sequential x values for each y value.

# get_time_deltas Module
* This module will create a list of time deltas given a list of datetime strings
that are provided in a file, one per line, assuming they are in ascending
order.
  * `./get_time_deltas.py test_data/dev_dtm_1s`
  ## get_dtm_data()
    * Returns an array of dtm strings, given the filename.
  ## calculate_deltas()
    * Return the time deltas, given an array of datetime strings.
