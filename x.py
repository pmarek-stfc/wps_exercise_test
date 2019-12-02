import xarray as xr
from itertools import combinations


def _get_years(dataset):
    REQ_YEARS = set([int(_) for _ in range(2010, 2020)])
    ds = xr.open_dataset(dataset)
    years = set([int(_) for _ in ds.time.dt.year])

    if REQ_YEARS.issubset(years):
        return dataset

def get_years(fpaths):
    files_in_range = []

    for fpath in fpaths:
        processed_file = _get_years(fpath)
        if processed_file is not None:
            files_in_range.append(processed_file)
    return files_in_range

# def couple_subset(files):
#     """ Returns all possible couples of files """
#     couple = 2
#     return list(combinations(files, couple))


def open_mfdatasets(files_to_open):
    """
        Test if a couple of data sets can be aggregated together
        and add them into a set if so
        :param files_to_open: found netCDF4 files
        :return: opened netCDF data sets using `open_mfdataset`
    """
    try:
        with xr.open_mfdataset(files_to_open, combine='by_coords') as ds:
            return ds
    except Exception as e:
        return e
