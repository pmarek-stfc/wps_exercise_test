import unittest
import x
import glob
import os


class X(unittest.TestCase):

    def test_get_years(self):
        file1 = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp45_r1i1p1_205512-208011.nc'
        file2 = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/tas_Amon_HadGEM2-ES_rcp45_r1i1p1_200512-203011.nc'
        file_path1 = os.path.join(os.environ.get('HOME'), file1)
        file_path2 = os.path.join(os.environ.get('HOME'), file2)

        years_none = x.get_years(file_path1)
        self.assertIsNone(years_none)

        years, years_desired = x.get_years(file_path2)
        self.assertIsNotNone(years, years_desired)
        self.assertTrue(len(years) > len(years_desired))

    def test_couple_subset(self):
        file = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/*.nc'
        file_path = os.path.join(os.environ.get('HOME'), file)
        files = glob.glob(file_path)
        result = x.couple_subset(files)
        self.assertIsNotNone(result)

    def test_open_mfdatasets(self):
        file = 'badc/cmip5/data/cmip5/output1/MOHC/HadCM3/rcp45/mon/atmos/Amon/r1i1p1/latest/tas/*.nc'
        file_path = os.path.join(os.environ.get('HOME'), file)
        files = glob.glob(file_path)

        files_to_open = x.couple_subset(files)
        result = x.open_mfdatasets(files_to_open)
        self.assertIsNotNone(result)


if __name__ == '__name__':
    unittest.main()