# asc2netcdf
Reads in asc grid files acts as a simple driver that parses ascii grid data.
Mainly used to read in the asc header data to.

The script was written to access the header and to calculate the upper right
corner centre of a grid. Some information form the header is particularily useful when setting up NetCdf files. e.g. number of rows and coloumns ect.
There is a simple function to read the header and spits out a named tuple.

```
import asc_reader

header = asc2netcdf.read_header('../data/test_data.asc')

header.cellsize
0.05
header.ncols
3
header.nrows
3
```
Information you can access.

```
header.ncols
header.nrows
header.xllcorner
header.yllcorner
header.cellsize 
header.nodata
header.xulcentre
header.yulcentre
header.xlrcentre
header.ylrcentre
```

There is a function that has been created to add the data to an existing NetCDF file. The function will also take gzip files as well and load them into the netCDF file.

addasc2nc
It takes four arguments are:
    filename: an asc to add to the netcdf file
    netcdf file handle: an open netCDF Dataset object
    variable: the variable in the netCDF dataset you want to add to e.g. rain
    time delta: the number of days since the start date of the netcdf file.

```
import asc2netcdf
from netCDF4 import Dataset

ascfile = 'testdata0.asc'
ncfilehandle = Dataset('test.nc', 'a')
variable = 'rain'
timedelta = 0 # first piece of data in the time dimention

asc_reader.addasc2nc(ascfile, ncfilehandle, variable, timedelta)
ncfilehandle.close()
```


# Credits #
Some test data provided by Wellington Regional Counicl and Landcare New Zealand under creative commons license. 