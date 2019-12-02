from x import get_years, open_mfdatasets
import glob
import time
import os
import cftime
from pathlib import Path
import pandas as pd
import xarray as xr
start_time = time.time()
max_lon, min_lon, max_lat, min_lat = 120, 80, 60, -60
files_path = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas'
absolute_path = os.path.join(str(Path.home()), files_path)
files = glob.glob(absolute_path + '/*.nc')
# #



if __name__=='__main__':
    d1 = cftime.Datetime360Day(2005, 1, 1)
    d2 = cftime.Datetime360Day(2100, 1, 1)
    # files_to_work_with = get_years(files)
    y = open_mfdatasets(files)
    # print(type(y))
    # print(len(y))
    # print(y)
    # print(y)
    # files_to_open = couple_subset(files_to_work_with)
    # print(files_to_open)
    # new_dataset = open_mfdatasets(files_to_open[5])
    # print(new_dataset.variables['time'])
    x = y.sel(time=slice(d1, d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
    # calculate temporal average across the time axis only
    mean_array = x.mean(dim='time')
    print(mean_array)
    mean_array.to_netcdf('result.nc')
    # print(mean_array.tas[0,0])
    # print(mean_array)
    # for i in x:
    #     print(i)

    print(f'took {time.time() - start_time} seconds')

