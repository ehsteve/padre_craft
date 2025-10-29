"""Provides functions to upload data to the time series database for display"""

from astropy.timeseries import TimeSeries
from swxsoc.util.util import record_timeseries


def record_housekeeping(hk_ts: TimeSeries, data_type):
    """Send the housekeeping time series to AWS."""
    record_timeseries(hk_ts, data_type, "craft")
