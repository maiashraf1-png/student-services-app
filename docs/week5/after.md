# Week 5 Before / After

| Measure | Before (legacy_fees.py) | After (fees.py) |
|---|---|---|
| Ruff issues (total) | 17 | 0 |
| Highest cyclomatic complexity | 9 (calc) | 3 (tuition_fee) |
| Arguments of the main function | 6 | 5 |
| Pylint score (/10) | 4.86 | 8.33 |
| Tests passing | 0 (no tests) | 16 passed |

Note: Ruff reported 17 problems instead of 16 because the newer Ruff version also reports PLR0917.

The remaining Pylint messages on fees.py are only missing docstrings.

## Pairing reflection
Working as driver and navigator helped us catch mistakes quickly. The navigator noticed naming problems and missing edge cases while the driver was typing. Switching roles kept both of us involved, and the tests let us change the code without fear of breaking it.
