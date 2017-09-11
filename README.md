# asc-reader
Reads in asc grid files acts as a simple driver that parses ascii grid data.
Mainly used to read in the asc header data to.

The script was written to access the header and to calculate the upper right
corner centre of a grid. Then this is used with nupmy to load the data into
netCDF files.

There is a simple function to read the header.

```
import asc_reader

header = asc_reader.read_header('../data/test_data.asc')

header.cellsize
0.05
header.ncols
3
header.nrows
3
```
Information you can access.

headr.ncols
header.nrows
header.xllcorner
header.yllcorner
header.cellsize 
header.nodata
header.upperrightcentrex
header.upperrightcentrey



# Credits #
Some test data provided by Wellington Regional Counicl and Landcare New Zealand under creative commons license. 