# mynumpkg

Simple NumPy-based array operations and statistics, written to practise
Python packaging (MPM Lecture 5, Exercise 2).

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from mynumpkg import elementwise_divide, summary_stats

elementwise_divide([2, 4], [1, 2])   # array([2., 2.])
summary_stats([1, 2, 3, 4])          # (2.5, 2.5, 1.118...)
```

## License

MIT, see `LICENSE`.
