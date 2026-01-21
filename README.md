# Package Sorting Solution

A Python solution for Thoughtful's robotic automation factory that dispatches packages to the correct stack based on their volume, dimensions, and mass.

## Problem Description

The robotic arm needs to sort packages into three different stacks:

- **STANDARD**: Standard packages that can be handled normally (not bulky and not heavy)
- **SPECIAL**: Packages that require special handling (either heavy or bulky, but not both)
- **REJECTED**: Packages that are both heavy and bulky and must be rejected

### Classification Rules

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is greater than or equal to 1,000,000 cm³, OR
  - Any of its dimensions (width, height, or length) is greater than or equal to 150 cm

- A package is **heavy** if:
  - Its mass is greater than or equal to 20 kg

## Installation

No external dependencies are required. This solution uses only Python's standard library.

**Requirements:**
- Python 3.6 or higher

## Usage

### Basic Usage

```python
from package_sorter import sort

# Standard package (small, light)
result = sort(10, 10, 10, 5)
print(result)  # Output: "STANDARD"

# Special package (bulky but not heavy)
result = sort(150, 10, 10, 5)
print(result)  # Output: "SPECIAL"

# Special package (heavy but not bulky)
result = sort(10, 10, 10, 20)
print(result)  # Output: "SPECIAL"

# Rejected package (both heavy and bulky)
result = sort(150, 10, 10, 20)
print(result)  # Output: "REJECTED"
```

### Function Signature

```python
def sort(width, height, length, mass) -> str
```

**Parameters:**
- `width` (float): Width of the package in centimeters
- `height` (float): Height of the package in centimeters
- `length` (float): Length of the package in centimeters
- `mass` (float): Mass of the package in kilograms

**Returns:**
- `str`: The stack name where the package should go ("STANDARD", "SPECIAL", or "REJECTED")

## Examples

### Example 1: Standard Package
```python
# Small package, light weight
sort(50, 50, 50, 10)  # Returns "STANDARD"
```

### Example 2: Bulky Package (Volume)
```python
# Large volume (1,000,000 cm³) but light weight
sort(100, 100, 100, 10)  # Returns "SPECIAL"
```

### Example 3: Bulky Package (Dimension)
```python
# One dimension >= 150 cm but light weight
sort(150, 50, 50, 10)  # Returns "SPECIAL"
```

### Example 4: Heavy Package
```python
# Heavy but small dimensions
sort(10, 10, 10, 20)  # Returns "SPECIAL"
```

### Example 5: Rejected Package
```python
# Both heavy and bulky
sort(150, 100, 100, 25)  # Returns "REJECTED"
```

## Running Tests

The solution includes a comprehensive test suite covering all classification categories and edge cases.

### Using unittest (Python standard library)

```bash
python -m unittest test_package_sorter.py
```

Or simply:

```bash
python test_package_sorter.py
```

### Expected Test Output

```
...............
----------------------------------------------------------------------
Ran 15 tests in 0.001s

OK
```

## Test Coverage

The test suite includes:

- **Standard packages**: Various sizes and weights that don't meet bulky or heavy criteria
- **Special packages**: Packages that are either bulky or heavy (but not both)
- **Rejected packages**: Packages that are both heavy and bulky
- **Boundary conditions**: Exactly at thresholds (1,000,000 cm³, 150 cm, 20 kg)
- **Edge cases**: Very small/large packages, floating point values, zero dimensions

## Code Quality

- Clean, readable code with clear variable names
- Comprehensive docstrings following Google style
- Type hints in docstrings
- Well-organized test cases with descriptive names
- Handles edge cases appropriately

## Solution Approach

The solution implements a straightforward classification algorithm:

1. Calculate the package volume (width × height × length)
2. Determine if the package is bulky (volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm)
3. Determine if the package is heavy (mass ≥ 20 kg)
4. Classify based on the combination:
   - Both heavy and bulky → "REJECTED"
   - Either heavy or bulky → "SPECIAL"
   - Neither heavy nor bulky → "STANDARD"

## Files

- `package_sorter.py`: Main implementation with the `sort()` function
- `test_package_sorter.py`: Comprehensive test suite
- `README.md`: This documentation file
