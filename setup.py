#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='asc2netcdf',
      version='0.1',
      description='Reads asc data into netCDF files',
      long_description=('The script was written to access the header and to \
      calculate the upper right corner centre of a grid. Some information \
      form the header is particularily useful when setting up NetCdf files.\
      e.g. number of rows and coloumns ect. There is a simple function to \
      read the header and spits out a named tuple.'),
      classifiers=[
          'Development Status :: 3 Alpha',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering :: GIS',
      ],
      keywords='GIS netCDF',
      url='https://github.com/andy3092/asc2netcdf',
      author='Andrew Rae',
      email='andrew3092@gmail.com',
      license='GPL',
      packages=find_packages(),
      install_requires=[
          'numpy',
          'netCDF4',
          'pytest',
      ],
      include_package_data=True,
      zip_safe=False)
