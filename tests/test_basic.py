#!/usr/bin/env python3

from context import asc_reader

testfile = asc_reader.readheader('../data/test_data.asc')
linztestfile = asc_reader.readheader(
    '../data/wellington-lidar-1m-dem-2013.asc')

def tessst_read_header_ncols():
    assert(testfile.ncols == 3)
    assert(linztestfile.ncols == 398)

def test_read_header_nrows():
    assert(testfile.nrows == 3)
    assert(linztestfile.nrows == 287)

def test_read_header_xllcorner():
    assert(testfile.xllcorner == 166.00)
    assert(linztestfile.xllcorner == 174.818018493000)

def test_read_header_yllcorner():
    assert(testfile.yllcorner == -47.600000000000)
    assert(linztestfile.yllcorner == -41.313597643208)


def test_read_header_cellsize():
    assert(testfile.cellsize == 0.05)
    assert(linztestfile.cellsize == 0.000010273382)

def test_read_header_nodata():
    assert(testfile.nodata == -9999.0)
    assert(linztestfile.nodata == -9999.0)

def test_read_header_xurcentre():
    assert(testfile.xulcentre == 166.025)
    assert(linztestfile.xulcentre == 174.818023629691)

def test_read_header_yulcentre():
    assert(testfile.yulcentre == -47.475)

def test_read_header_xlrcentre():
    assert(testfile.xlrcentre == 166.125)

def test_read_header_ylrcentre():
    assert(testfile.ylrcentre == -47.575)


