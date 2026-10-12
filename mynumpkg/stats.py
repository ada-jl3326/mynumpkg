"""Basic statistics of NumPy arrays."""

import numpy as np

__all__ = ['summary_stats']


def summary_stats(a):
    """
    Compute the mean, median and standard deviation of an array.

    Parameters
    ----------
    a : array_like
        The input values.

    Returns
    -------
    tuple of float
        ``(mean, median, std)`` of `a`, where ``std`` is the population
        standard deviation (``ddof=0``).
    """
    a = np.asarray(a)
    return np.mean(a), np.median(a), np.std(a)
