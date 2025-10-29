import numpy as np
import pytest
from astropy.timeseries import TimeSeries

import padre_craft.io.file_tools as file_tools
from padre_craft import _test_files_directory

test_file_paths = _test_files_directory.glob("*.csv")


@pytest.mark.parametrize("this_path", list(test_file_paths))
def test_file_read(this_path):
    """Test that all test files can be read"""
    data = file_tools.read_file(this_path)
    assert isinstance(data, TimeSeries)
    assert len(data) == 9  # check all data was read
    assert len(np.unique(data.time)) == 9  # check all times are unique
    data = file_tools.read_raw_file(this_path)
    assert isinstance(data, TimeSeries)
    assert len(data) == 9
    assert len(np.unique(data.time)) == 9
