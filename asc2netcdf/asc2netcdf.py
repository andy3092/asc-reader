#!/usr/bin/env python3
import linecache
import collections
import time
import platform
import getpass
import numpy as np
from netCDF4 import Dataset

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
    ymax_center = ymax - (cellsize / 2)
    xmax_center = xmax - (cellsize / 2)
    ymin_center = yllcorner + (cellsize / 2)

    return Header(ncols=ncols, nrows=nrows,
                  xllcorner=xllcorner, yllcorner=yllcorner,
                  cellsize=cellsize, nodata=nodata,
                  xmax_center=xmax_center, ymax_center=ymax_center,
                  xmin_center=xmin_center, ymin_center=ymin_center,
                  xmin=xllcorner, xmax=xmax, ymin=yllcorner, ymax=ymax)


def create_nc(filename, template, title, start_time, x='lon', y='lat',
              x_standard_name='longitude', y_standard_name='latitude',
              y_units='degrees_north', x_units='degrees_east'):
    """
    Creates an nc file which uses an asc file as a template to create the
    dimentions of the new file. The file will contain a bare bones netCDF file.

    filename:
            The name of the new netCDF file to be created.
    template: 
            Name of the file to be used create the location information
            and the dimentions for the netCDF file.
    title:
            Title of the NetCDF file
    start_time:  
            Start time of the netCDF file.

    Extra metadata will need to be added to the file. 
    """
    # Create netcdf file
    asc_header = readheader(template)
    rootgrp = Dataset(filename, "w", format="NETCDF4")

    # Add general metadata to the file.
    rootgrp.history = 'Created ' + time.ctime(time.time())
    rootgrp.history = rootgrp.history + ' OS: ' +  platform.platform()
    rootgrp.history = rootgrp.history + ' User: ' +  getpass.getuser()
    rootgrp.title = title
    rootgrp.source = ('Created with ' + __name__ + ' using ' +
                      template + 'as a template.')
    rootgrp.conventions = 'CF-1.6'

    # create the dimentions
    rootgrp.createDimension(x, asc_header.ncols) # x
    rootgrp.createDimension(y, asc_header.nrows) # y
    rootgrp.createDimension('time', None) # time

    # create the variables
    x_variable = rootgrp.createVariable(x, 'f4',(x,))
    y_variable = rootgrp.createVariable(y, 'f4',(y,))
    time_variable = rootgrp.createVariable('time', 'f8', ('time',))

    # variable metadata
    x_variable.units = x_units
    y_variable.units = y_units
    x_variable.standard_name = x_standard_name
    y_variable.standard_name = y_standard_name
    time_variable.units = start_time
    time_variable.calendar = "gregorian"
    
    # Inatise the lat long data
    # need to add the cell size
    x_coordinates = np.linspace(asc_header.xmin_center,
                      asc_header.xmax_center,
                      asc_header.ncols)
    
    y_coordinates = np.linspace(asc_header.ymax_center,
                      asc_header.ymin_center,
                      asc_header.nrows)

    y_variable[:] = y_coordinates
    x_variable[:] = x_coordinates
    rootgrp.close()

    
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
