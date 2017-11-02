#!/usr/bin/env python3

import os
from netCDF4 import Dataset
from context import asc2netcdf
import numpy as np

testbasename = 'data/testdata'
testfile = asc2netcdf.readheader('data/test_data.asc')
netCDFfile = 'data/test.nc'


# Need to copy file template over before starting test
linztestfile = asc2netcdf.readheader(
    'data/wellington-lidar-1m-dem-2013.asc')


def tessst_read_header_ncols():
    assert(testfile.ncols == 3)
    assert(linztestfile.ncols == 398)


def test_read_header_nrows():
    assert(testfile.nrows == 3)
    assert(linztestfile.nrows == 287)

           
def test_read_header_cellsize():
    assert(testfile.cellsize == 0.05)
    assert(linztestfile.cellsize == 0.000010273382)


def test_read_header_xllcorner():
    assert(testfile.xllcorner == 166.00)
    assert(linztestfile.xllcorner == 174.818018493000)

    
def test_read_header_xmin():
    assert(testfile.xmin == 166.00)
    assert(linztestfile.xmin == 174.818018493000)


def test_read_header_xmax():
    assert(testfile.xmax == 166.150)
    

def test_read_header_yllcorner():
    assert(testfile.yllcorner == -47.600000000000)
    assert(linztestfile.yllcorner == -41.313597643208)


def test_read_header_ymin():
    assert(testfile.ymin == -47.600000000000)
    assert(linztestfile.ymin == -41.313597643208)
    assert(testfile.ymin < testfile.ymax)

def test_read_header_ymax():
    assert(testfile.ymax == -47.4500000000000)
    assert(testfile.ymax > testfile.ymin)
    
def test_read_header_nodata():
    assert(testfile.nodata == -9999.0)
    assert(linztestfile.nodata == -9999.0)


def test_read_header_xmax_center():
    assert(testfile.xmax_center == 166.125)
    assert(linztestfile.xmax_center == 174.82210216234503)
    assert(testfile.xmax_center > testfile.xmin_center)


def test_read_header_ymax_center():
    assert(testfile.ymax_center == -47.475)
    assert(testfile.ymax_center > testfile.ymin_center)

def test_read_header_xmin_center():
    assert(testfile.xmin_center == 166.025)
    assert(testfile.xmin_center < testfile.xmax_center)

def test_read_header_ymin_center():
    assert(testfile.ymin_center == -47.575)
    assert(testfile.ymin_center < testfile.ymax_center)

def test_create_nc():
    template = testbasename + '1.asc'
    testfile = 'testfile.nc'
    asc2netcdf.create_nc(testfile, template, 'Test', 'days since 1960-1-1')
    ncfile = Dataset(testfile, 'r')
    lat = ncfile.variables['lat'][:]
    lon = ncfile.variables['lon'][:]

    # check the title
    assert(ncfile.title == 'Test')
    
    # check the number of columns
    assert(lat.size == 271)
    assert(lon.size == 279)

    # assert min and max values for lat
    np.testing.assert_allclose(lat.max(), -34.075)
    np.testing.assert_allclose(lat.min(), -47.575)

    # assert min and max values for lon
    np.testing.assert_allclose(lon.min(), 166.025)
    np.testing.assert_allclose(lon.max(), 179.925)
    os.remove(testfile)

def test_addasc2ncdata():
    for i in range(4):
        testfilename = testbasename + '%d.asc' % (i)
        data = np.loadtxt(testfilename, skiprows=6)
        ncfile = Dataset(netCDFfile, 'r')
        ncdata = ncfile.variables['rain'][i, :, :]
        

        # Check the arrays match 
        np.testing.assert_array_almost_equal(ncdata, data)
    ncfile.close()
