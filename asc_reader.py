#!/usr/bin/env python3
import linecache
import collections

def readheader(filename):
    """
    Takes a file name and reads the header of the file
    First implemented as a named tuple. So you can call 
    a = read_header('myfile.asc')
    a.cellsize ...
    """
    tuplefields = ('ncols nrows xllcorner yllcorner cellsize nodata '
                   'xulcentre yulcentre xlrcentre ylrcentre')
    
    Header = collections.namedtuple('Header', tuplefields)
    ncols = int(linecache.getline(filename, 1).split()[1])
    nrows = int(linecache.getline(filename, 2).split()[1])
    xllcorner = float(linecache.getline(filename, 3).split()[1])
    yllcorner = float(linecache.getline(filename, 4).split()[1])
    cellsize = float(linecache.getline(filename, 5).split()[1])
    nodata = float(linecache.getline(filename, 6).split()[1])

    gridheight = nrows * cellsize
    gridwidth = ncols * cellsize

    xulcentre = xllcorner + (cellsize / 2)
    yulcentre = yllcorner - (cellsize / 2) + gridheight
    xlrcentre = xllcorner - (cellsize / 2) + gridwidth
    ylrcentre = yllcorner + (cellsize / 2)


    return Header(ncols=ncols, nrows=nrows,
                  xllcorner=xllcorner, yllcorner=yllcorner,
                  cellsize=cellsize, nodata=nodata,
                  xulcentre=xulcentre, yulcentre=yulcentre,
                  xlrcentre=xlrcentre, ylrcentre=ylrcentre)




        
