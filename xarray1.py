import xarray as xr
from x import get_years, couple_subset, open_mfdatasets
import glob
import time
from datetime import datetime
import cftime

start_time = time.time()
max_lon, min_lon, max_lat, min_lat = 120, -120, 60, -60
file1 = '/home/pmarek/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp45_r1i1p1_200512-203011.nc'
files = glob.glob('/home/pmarek/badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/*.nc')
# a = couple_subset(files)
# print(len(a))
# # ds.sel(lon=(ds.lon < -80) | (ds.lon > 40))
#
#
files_to_open = couple_subset(files)
new_set = open_mfdatasets(files_to_open)
length_lon_dims = new_set.dims['lon']
array = new_set.roll(lon=int(length_lon_dims/2), roll_coords=True)
new_coords = array[0: int(length_lon_dims/2)].assign_coords(lon=(360.0 - array[0: int(length_lon_dims/2)]['lon']))
print(new_coords)
#x = new_set['time'].isel(time = slice('2010-01-01', '2020-01-01'))
t = new_set['time']
#print(t[0].values,t[0].values.dtype)
# print(t.to_datetimeindex())
d1=cftime.Datetime360Day(2010,1,1)
d2=cftime.Datetime360Day(2020,1,1)
# x = new_coords['tas'].sel(time=slice(d1,d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
# print(x)

#print(x)
#

#monthly = new_set.where(new_set['time.year'] > 2000, drop=True).groupby('time.month').mean('time')
# x = a.sel(time=slice('2010-01-01', '2020-01-01'))
# print(x)
print(f'took {time.time() - start_time} seconds')

