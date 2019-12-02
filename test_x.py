import unittest
import x
import glob
import os
from x import open_mfdatasets
import cftime
from pathlib import Path

max_lon, min_lon, max_lat, min_lat = 120, 80, 60, -60
d1 = cftime.Datetime360Day(2010, 1, 1)
d2 = cftime.Datetime360Day(2020, 1, 1)

def calc_temporal_avg_one():
    """ calculate temporal average across the time axis only
        FOR ONE FILE """
    files_path = 'xarray/tas_Amon_HadGEM2-CC_rcp45_r1i1p1_200512-203011.nc'
    absolute_path = os.path.join(str(Path.home()), files_path)
    y = open_mfdatasets(absolute_path)
    x = y.sel(time=slice(d1, d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
    # calculate temporal average across the time axis only
    mean_array = x.mean(dim='time')
    # print(mean_array)
    return mean_array


def calc_temporal_avg_multiple():
    """ calculate temporal average across the time axis only
        FOR MORE FILES"""
    files_path = 'xarray'
    absolute_path = os.path.join(str(Path.home()), files_path)
    files = glob.glob(absolute_path + '/*.nc')
    y = open_mfdatasets(files)
    x = y.sel(time=slice(d1, d2), lon=slice(min_lon, max_lon), lat=slice(min_lat, max_lat))
    # calculate temporal average across the time axis only
    mean_array = x.mean(dim='time')
    # print(mean_array)
    return mean_array


class X(unittest.TestCase):

    # def test_get_years(self):
    #     file1 = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp45_r1i1p1_205512-208011.nc'
    #     file2 = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp45_r1i1p1_200512-203011.nc'
    #     file_path1 = os.path.join(os.environ.get('HOME'), file1)
    #     file_path2 = os.path.join(os.environ.get('HOME'), file2)
    #
    #     years_none = x.get_years(file_path1)
    #     self.assertIsNone(years_none)
    #
    #     years, years_desired = x.get_years(file_path2)
    #     self.assertIsNotNone(years, years_desired)
    #     self.assertTrue(len(years) > len(years_desired))
    #
    #
    #
    # def test_couple_subset(self):
    #     file = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/*.nc'
    #     file_path = os.path.join(os.environ.get('HOME'), file)
    #     files = glob.glob(file_path)
    #     result = x.couple_subset(files)
    #     self.assertIsNotNone(result)

    # def test_open_mfdatasets(self):
    #     file = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/*.nc'
    #     file_path = os.path.join(os.environ.get('HOME'), file)
    #     files = glob.glob(file_path)
    #
    #     files_to_open = x.couple_subset(files)
    #     result = x.open_mfdatasets(files_to_open)
    #     self.assertIsNotNone(result)

    def test_open_mfdatasets(self):
        """
            Test to calculate temporal average across the time axis only
        """
        self.assertIsNotNone(calc_temporal_avg_one())

    def test_error(self):
        """
            Test if calc_temporal_avg() throws a KeyError when
            calculating temporal average on aggregated .nc files
            ERROR - KeyError: cftime.Datetime360Day(2010-01-01 00:00:00)
            when Xarray's function "open_mfdataset" does not include
            combine='by_coords'
        """
        with self.assertRaises(KeyError): calc_temporal_avg_multiple()


if __name__ == '__name__':
    unittest.main()