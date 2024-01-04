#!/usr/bin/python3
""" This is a pascals triangle method """
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Parameters:
    n (int): Number of rows in the triangle. Must be an integer.

    Returns:
    list: A list of lists of integers representing Pascal's triangle up to n rows.
          Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []  # Return an empty list if n <= 0

    # Initialize triangle with the first row
    triangle = [[1]]

    # Generate each row in the triangle
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        last_row = triangle[-1]  # Get the last row of the triangle

        # Each element (excluding the first and last of each row)
        # is the sum of the two elements directly above it
        row += [last_row[j] + last_row[j+1] for j in range(len(last_row) - 1)]
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the row to the triangle

    return triangle

