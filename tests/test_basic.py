#!/usr/bin/env python3

from context import asc_reader

testfile = asc_reader.readheader('../data/test_data.asc')
linztestfile = asc_reader.readheader(
    '../data/wellington-lidar-1m-dem-2013.asc')

ascfile = asc_reader.AscFile('../data/test_data.asc')

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

def test_read_header_upperrightcentrex():
    assert(testfile.upperrightcentrex == 166.025)
    assert(linztestfile.upperrightcentrex == 174.818023629691)

def test_read_header_upperrightcentrey():
    assert(testfile.upperrightcentrey == -47.475)
    #assert(linztestfile.upperrightcentrey == )

def test_AscFile_data():
    assert(ascfile.data.size == 9)
    assert(ascfile.data.shape == (3, 3))
    #assert(asctestfile.data.size == 114226)
    #assert(asclinztestfile.data.shape == (287, 398))

