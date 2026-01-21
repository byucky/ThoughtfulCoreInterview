"""
Package Sorting Module for Robotic Automation Factory

This module provides functionality to sort packages into appropriate stacks
based on their dimensions and mass.
"""

from typing import Union, Literal


def sort(
    width: Union[float, int],
    height: Union[float, int],
    length: Union[float, int],
    mass: Union[float, int]
) -> Literal["STANDARD", "SPECIAL", "REJECTED"]:
    """
    Sort a package into the appropriate stack based on its dimensions and mass.
    
    A package is classified as:
    - BULKY: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
    - HEAVY: mass >= 20 kg
    
    Packages are dispatched to:
    - STANDARD: standard packages (not bulky and not heavy)
    - SPECIAL: packages that are either heavy or bulky (but not both)
    - REJECTED: packages that are both heavy and bulky
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
    
    Returns:
        str: The stack name where the package should go ("STANDARD", "SPECIAL", or "REJECTED")
    
    Examples:
        >>> sort(10, 10, 10, 5)
        'STANDARD'
        >>> sort(150, 10, 10, 5)
        'SPECIAL'
        >>> sort(10, 10, 10, 20)
        'SPECIAL'
        >>> sort(150, 10, 10, 20)
        'REJECTED'
    """
    # Calculate volume
    volume = width * height * length
    
    # Check if bulky: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if heavy: mass >= 20 kg
    is_heavy = mass >= 20
    
    # Classify package
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"
