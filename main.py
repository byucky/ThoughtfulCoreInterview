#!/usr/bin/env python3
"""
Main entry point for the package sorting application.

Allows users to input package dimensions and mass to get the classification.
"""

import sys
from package_sorter import sort


def get_numeric_input(prompt, param_name):
    """
    Get numeric input from user with proper error handling.
    
    Args:
        prompt (str): The prompt to display to the user
        param_name (str): Name of the parameter for error messages
    
    Returns:
        float: The numeric value entered by the user
    """
    while True:
        try:
            value = input(prompt)
            # Strip whitespace
            value = value.strip()
            
            # Check if empty
            if not value:
                print(f"Error: {param_name} cannot be empty. Please enter a numeric value.")
                continue
            
            # Try to convert to float
            numeric_value = float(value)
            
            # Check for negative values (warn but allow)
            if numeric_value < 0:
                print(f"Warning: {param_name} is negative ({numeric_value}). This may not be physically meaningful.")
                response = input("Continue anyway? (y/n): ").strip().lower()
                if response not in ['y', 'yes']:
                    continue
            
            return numeric_value
            
        except ValueError:
            print(f"Error: '{value}' is not a valid number. Please enter a numeric value for {param_name}.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled.")
            sys.exit(0)


def parse_command_line_args():
    """
    Parse command line arguments with detailed error handling.
    
    Returns:
        tuple: (width, height, length, mass) if successful
    """
    param_names = ["width", "height", "length", "mass"]
    values = []
    
    for i, param_name in enumerate(param_names, 1):
        try:
            value = float(sys.argv[i])
            
            # Check for negative values
            if value < 0:
                print(f"Warning: {param_name} is negative ({value}). This may not be physically meaningful.")
            
            values.append(value)
        except ValueError:
            print(f"Error: Invalid value for {param_name}: '{sys.argv[i]}'")
            print(f"       {param_name} must be a numeric value (integer or decimal).")
            print_usage()
            sys.exit(1)
    
    return tuple(values)


def main():
    """Main function to run the package sorter interactively or via command line."""
    if len(sys.argv) == 5:
        # Command line arguments provided
        width, height, length, mass = parse_command_line_args()
    else:
        # Interactive mode
        print("Package Sorting System")
        print("=" * 50)
        print("Enter package dimensions and mass to get classification.")
        print("(You can enter integers or decimal numbers)\n")
        
        width = get_numeric_input("Enter width (cm): ", "width")
        height = get_numeric_input("Enter height (cm): ", "height")
        length = get_numeric_input("Enter length (cm): ", "length")
        mass = get_numeric_input("Enter mass (kg): ", "mass")
    
    # Calculate and display result
    result = sort(width, height, length, mass)
    
    print("\n" + "=" * 50)
    print(f"Package Classification: {result}")
    print("=" * 50)
    
    # Display package details
    volume = width * height * length
    print(f"\nPackage Details:")
    print(f"  Dimensions: {width} cm × {height} cm × {length} cm")
    print(f"  Volume: {volume:,.0f} cm³")
    print(f"  Mass: {mass} kg")
    
    # Show why it was classified this way
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    print(f"\nClassification Logic:")
    print(f"  Bulky: {is_bulky} (volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm)")
    print(f"  Heavy: {is_heavy} (mass ≥ 20 kg)")
    
    return result


def print_usage():
    """Print usage instructions."""
    print("\nUsage:")
    print("  Interactive mode: python main.py")
    print("  Command line:     python main.py <width> <height> <length> <mass>")
    print("\nExample:")
    print("  python main.py 100 100 100 20")
    print("  python main.py 150 10 10 5")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "help"]:
        print_usage()
        sys.exit(0)
    
    main()
