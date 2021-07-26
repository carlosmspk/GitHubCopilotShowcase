"""
This program produces a sphere in ASCII art.
Using the "*" the program prints an approximation of a sphere for a given radius
"""

def sphere(radius : int) -> str:
    """>>>
    Returns a string of a sphere of radius "radius" using * as ASCII art
    """
    # The sphere is a list of strings
    sphere = []
    # The loop runs from -radius to radius+1
    for i in range(-radius, radius+1):
        # The inner loop runs from -radius to radius+1
        for j in range(-radius, radius+1):
            # The "*" is the ASCII art of a sphere
            if i**2 + j**2 <= radius**2:
                sphere.append("*")
            else:
                sphere.append(" ")
        # The line is a string of the current row
        line = "".join(sphere)
        # The list is a string of the current row
        sphere = [line]
    # The final row of the string is a string of the entire sphere
    return "\n".join(sphere)

#>>> Print sphere with radius 5
print(sphere(5))