from x import get_years, couple_subset, open_mfdatasets
import glob
import time
import os
import cftime
from pathlib import Path


start_time = time.time()
max_lon, min_lon, max_lat, min_lat = 120, 80, 60, -60

files_path = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas'
absolute_path = os.path.join(str(Path.home()), files_path)
files = glob.glob(absolute_path + '/*.nc')

#

if __name__=='__main__':
    d1 = cftime.Datetime360Day(2010, 1, 1)
    d2 = cftime.Datetime360Day(2020, 1, 1)
    files_to_open = couple_subset(files)
    new_dataset = open_mfdatasets(files_to_open)


    x = new_dataset['tas'].sel(time=slice(d1, d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
    mean_array = x.mean()
    print(mean_array.values)
    print(f'took {time.time() - start_time} seconds')






# new_set.coords['lon'] = (new_set.coords['lon'] + 180) % 360 - 180
# new_set = new_set.sortby(new_set.lon)
# print(new_set)



# ds_rolled = new_set.assign_coords(lon=(new_set.lon % 360)).roll(lon=(new_set.dims['lon'] // 2))
# print(ds_rolled)

# length_lon_dims = new_set.dims['lon']
# array = new_set.roll(lon=int(length_lon_dims // 2), roll_coords=True)
# print(array)

# print(array)
# a1 = new_set
# a2 = array
# a1_test = a1['tas'][0,0,:92].values
# a2_test = a2['tas'][0,0,92:].values
# print(a1_test == a2_test)
# pdb.set_trace()
# array.to_netcdf('2.nc')






# x = new_set.sel(time=slice(d1, d2))
# print(x)


