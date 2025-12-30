#!/usr/bin/env python3
# Created by: Brandon
# Created on: December 19th, 2025
# This program calculates the volume and surface area of a square pyramid

import math

# Function to calculate surface area
def calculate_Surface_Area(s_base, s_height):
    # Calculate and return the surface area of a square pyramid
    surface_area = s_base**2 + 2 * s_base * math.sqrt((s_base**2 / 4) + s_height**2)
    return surface_area

# Function to calculate volume
def calculate_Volume(v_base, v_height):
    # Calculate and return the volume of a square pyramid
    volume = (v_base**2) * v_height / 3
    return volume


def main():
    # Get Base and Height from the user
    try:
        base = float(input("Enter the base of the Square Pyramid: "))
        height = float(input("Enter the height of the Square Pyramid: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Call functions
    surface_area = calculate_Surface_Area(base, height)
    volume = calculate_Volume(base, height)

    # Display results
    print("The surface area of the Square Pyramid is: {:.2f}".format(surface_area))
    print("The volume of the Square Pyramid is: {:.2f}".format(volume))


if __name__ == "__main__":
    main()
