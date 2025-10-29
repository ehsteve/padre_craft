"""
Provides generic file readers.
"""

from pathlib import Path

import astropy.io.fits as fits
from astropy.io import ascii
from astropy.time import Time
from astropy.timeseries import TimeSeries

from padre_craft.util.util import filename_to_datatype

__all__ = ["read_file", "read_raw_file", "read_fits"]


def read_file(filename: Path):
    """
    Read a file.

    Parameters
    ----------
    filename: Path
        A file to read.

    Returns
    -------
    data

    Examples
    --------
    """
    # TODO: the following should use parse_science_filename
    this_path = Path(filename)
    match this_path.suffix.lower():
        case ".csv":  # raw binary file
            result = read_raw_file(this_path)
        case ".fits":  # level 0 or above
            result = read_fits(this_path)
        case _:
            raise ValueError(f"File extension {this_path.suffix} not recognized.")
    return result


def read_raw_file(file_path: Path) -> TimeSeries:
    """
    Read a raw (csv) data file.

    Parameters
    ---------
    filename : Path
        A file to read

    Returns
    -------
    ts : TimeSeries
        The timeseries data
    """
    if not isinstance(file_path, Path):
        file_path = Path(file_path)
    data_table = ascii.read(file_path, format="csv")
    time = Time(data_table["timestamp"], format="unix")
    ts = TimeSeries(time=time, data=data_table)
    ts.time.format = "isot"
    ts.meta.update({"filename": file_path.name})
    ts.meta.update({"data_type": filename_to_datatype(file_path.name)})
    ts.sort()
    return ts


def read_fits(filename: Path):
    """
    Read a fits file of any level and return the appropriate data objects.
    """
    hdul = fits.open(filename)
    # header = hdul[0].header.copy()

    return hdul
