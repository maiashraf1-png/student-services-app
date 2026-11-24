# Week 5 Findings

## 1. Findings table

Note: my Ruff version reports 17 problems (not 16) because it also reports PLR0917 (too-many-positional-arguments), which is the same problem as PLR0913.

| Rule | Count | Smell (lecture name) | Refactoring |
|---|---|---|---|
| F401 | 2 | Dead code (unused imports) | Delete the imports |
| PLR2004 | 6 | Magic numbers | Replace with named constants / an enum |
| C901 | 1 | Long method / complex conditionals | Replace the if/elif chain with a rate table; extract methods |
| PLR0913 | 1 | Long parameter list | Remove the unused argument; use a Course class instead of raw dictionaries |
| ARG001 | 1 | Dead code (unused argument `y`) | Remove the argument |
| B006 | 1 | Mutable default argument (hidden shared state) | Use an immutable default `extras=()` |
| E711 / E712 | 2 | Bad comparisons to None / True | Use `is not None` and `if summer:` |
| F841 | 1 | Dead code (unused variable `tmp`) | Delete the variable |
| N802 | 1 | Bad naming | Rename `ProcessAll` to `process_all` |

## 2. Smells Ruff did not report

1. Bad names: `d`, `t`, `s`, `y`, `c`, `e`, `x`, `st` do not explain anything.
2. Duplicated code: the two `calc(...)` calls in `ProcessAll` are almost identical, and the type if/elif structure is repeated in `calc` and `report`.
3. Mixed responsibilities: `report` calculates the fee and prints it in the same function.
4. Type codes (1/2/3) explained only by a comment instead of an Enum.
5. Primitive obsession: courses are plain dictionaries like `{"h": 3}`.

## 3. The hidden bug in ProcessAll

ProcessAll has an if for student type 1 and an if for type 2, but no case for type 3 (scholarship). For Omar, fee is never calculated, so it keeps the value from the previous student (Sara, 1050) instead of 0. If a scholarship student were first in the list, the code would crash because fee would not exist yet.