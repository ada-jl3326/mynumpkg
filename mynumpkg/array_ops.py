"""Element-wise operations on NumPy arrays."""

import numpy as np

__all__ = ['elementwise_multiply', 'elementwise_divide']


def elementwise_multiply(a, b):
    """
    Multiply two arrays element-wise.

    Parameters
    ----------
    a : array_like
        The first array.
    b : array_like
        The second array, with the same shape as `a`.

    Returns
    -------
    numpy.ndarray
        The element-wise product of `a` and `b`.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return a * b


def elementwise_divide(a, b):
    """
    Divide one array by another element-wise.

    Parameters
    ----------
    a : array_like
        The numerator.
    b : array_like
        The denominator, with the same shape as `a`.

    Returns
    -------
    numpy.ndarray
        The element-wise quotient ``a / b``.

    Raises
    ------
    ValueError
        If any element of `b` is zero.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    if np.any(b == 0):
        raise ValueError("b must not contain zeros")
    return a / b
