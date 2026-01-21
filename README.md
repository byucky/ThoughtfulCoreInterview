**Requirements:**
- Python 3.6 or higher

## Quick Start

### Using the Main Application

The easiest way to use the package sorter is through the main application, which provides both interactive and command-line interfaces.

#### Interactive Mode

Run the main script without arguments to enter interactive mode:

```bash
python main.py
```

You will be prompted to enter:
- Width (cm)
- Height (cm)
- Length (cm)
- Mass (kg)

The application will then display the package classification along with detailed information about why it was classified that way.

#### Command Line Mode

You can also provide all arguments directly via command line:

```bash
python main.py <width> <height> <length> <mass>
```

**Examples:**

```bash
# Standard package
python main.py 10 10 10 5

# Special package (bulky)
python main.py 150 10 10 5

# Special package (heavy)
python main.py 10 10 10 20

# Rejected package
python main.py 150 10 10 20
```

#### Help

To see usage instructions:

```bash
python main.py --help
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

## Function Signature

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

## Questions

- How should the pysically impossible edge cases be handled? 'REJECTED' | 'STANDARD' (e.g. sort(0,0,1,0) or even sort(1000000,1000000,1000000, 1) )
