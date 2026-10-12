"""Tests for mynumpkg."""

import numpy as np
import pytest

from mynumpkg import elementwise_divide, elementwise_multiply, summary_stats


class TestArrayOps:
    """Tests for the functions in array_ops.py."""

    @pytest.mark.parametrize('a, b, expected', [
        ([1, 2, 3], [4, 5, 6], [4, 10, 18]),
        ([0.5, -2], [4, 3], [2.0, -6.0]),
    ])
    def test_elementwise_multiply(self, a, b, expected):
        """elementwise_multiply multiplies element by element."""
        np.testing.assert_allclose(elementwise_multiply(a, b), expected)

    def test_elementwise_divide(self):
        """elementwise_divide divides element by element."""
        np.testing.assert_allclose(elementwise_divide([6, 9], [3, 4]),
                                   [2.0, 2.25])

    def test_elementwise_divide_by_zero(self):
        """elementwise_divide raises ValueError when b contains 0."""
        with pytest.raises(ValueError):
            elementwise_divide([1, 2], [1, 0])


class TestStats:
    """Tests for the functions in stats.py."""

    def test_summary_stats(self):
        """summary_stats gives the mean, median and population std."""
        mean, median, std = summary_stats([2, 4, 4, 4, 5, 5, 7, 9])
        assert mean == pytest.approx(5.0)
        assert median == pytest.approx(4.5)
        assert std == pytest.approx(2.0)
