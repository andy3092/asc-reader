#!/usr/bin/env python3
import linecache
import collections
import numpy as np


def readheader(filename):
    """
    Takes a file name and reads the header of the file
    First implemented as a named tuple. So you can call
    a = read_header('myfile.asc')
    a.cellsize ...
    """
    tuplefields = ('ncols nrows xllcorner yllcorner cellsize nodata '
                   'xmax_center ymax_center xmin_center ymin_center '
                   'xmin xmax ymin ymax')

    Header = collections.namedtuple('Header', tuplefields)
    ncols = int(linecache.getline(filename, 1).split()[1])
    nrows = int(linecache.getline(filename, 2).split()[1])
    xllcorner = float(linecache.getline(filename, 3).split()[1])
    yllcorner = float(linecache.getline(filename, 4).split()[1])
    cellsize = float(linecache.getline(filename, 5).split()[1])
    nodata = float(linecache.getline(filename, 6).split()[1])

    gridheight = nrows * cellsize
    gridwidth = ncols * cellsize

    # Calculate the max values for x and y
    
    ymax = yllcorner + gridheight
    xmax = xllcorner + gridwidth
    
    # Find the center point for the min and max values
    xmin_center = xllcorner + (cellsize / 2)
    ymax_center = yllcorner - (cellsize / 2) + gridheight
    xmax_center = xllcorner - (cellsize / 2) + gridwidth
    ymin_center = yllcorner + (cellsize / 2)

    return Header(ncols=ncols, nrows=nrows,
                  xllcorner=xllcorner, yllcorner=yllcorner,
                  cellsize=cellsize, nodata=nodata,
                  xmax_center=xmax_center, ymax_center=ymax_center,
                  xmin_center=xmin_center, ymin_center=ymin_center,
                  xmin=xllcorner, xmax=xmax, ymin=yllcorner, ymax=ymax)


def addasc2nc(filename, ncfilenamehandle, variable, timedelta):
    """
    Takes an ascfile and copies it into a netCDF file.
    The netCDF file must already exist and be open.
    You will need to know the number of days since the first day in the
    netcdf file.
    filename file: name of the ascfile
    ncfilehandle:  an open netCDF Dataset object
    variable:     name in the netCDF dataset you want to add to e.g. rain
    timedelta:    the number of days since the start date of the netcdf file.
    """
    ncfilenamehandle.variables['time'][timedelta] = timedelta
    data = np.loadtxt(filename, skiprows=6)
    ncfilenamehandle.variables[variable][timedelta, :, :] = data
    return
