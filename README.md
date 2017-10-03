# asc-reader
Reads in asc grid files acts as a simple driver that parses ascii grid data.
Mainly used to read in the asc header data to.

The script was written to access the header and to calculate the upper right
corner centre of a grid. Some information form the header is particularily useful when setting up NetCdf files. e.g. number of rows and coloumns ect.
There is a simple function to read the header and spits out a named tuple.

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


Data can be loaded into numpy using the following code np.loadtxt, then put intoa netCDF file. The example below has three dimentions time, lat and lon.

```
from netCDF4 import Dataset
netcdf_file = Dataset("my_netcdf.nc", "a")
netcdf_file.variables['time'][0] = 0
data = np.loadtxt('filename', skiprows=6)
netcdf_file.variables['my_variable'][0,:,:] = data
netcdf_file.close()
```

# Credits #
Some test data provided by Wellington Regional Counicl and Landcare New Zealand under creative commons license. 