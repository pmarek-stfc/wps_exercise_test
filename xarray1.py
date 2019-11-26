from x import get_years, couple_subset, open_mfdatasets
import glob
import time
import os
import cftime
from pathlib import Path


start_time = time.time()
max_lon, min_lon, max_lat, min_lat = 120, 80, 60, -60

# one_file = 'tas_Amon_HadGEM2-ES_rcp45_r1i1p1_203012-205511.nc'
files_path = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas'
absolute_path = os.path.join(str(Path.home()), files_path)
files = glob.glob(absolute_path + '/*.nc')
# #
# d1 = cftime.Datetime360Day(2010, 1, 1)
# d2 = cftime.Datetime360Day(2020, 1, 1)


if __name__=='__main__':
    print(get_years(files))

    # files_to_open = couple_subset(files)
    # new_dataset = open_mfdatasets(files_to_open)
    #
    # x = new_dataset['tas'].sel(time=slice(d1, d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
    # # calculate temporal average across the time axis only
    # mean_array = x.mean(dim='time')
    # for i in mean_array:
    #     print(i)

    print(f'took {time.time() - start_time} seconds')

