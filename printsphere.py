"""
This program produces a sphere in ASCII art.
Using the "*" the program prints an approximation of a sphere for a given radius
"""

def circle(radius : int) -> list:
    """>>>
    Returns a list of strings of a circle of radius "radius" using * as ASCII art. This is done using (x-xcenter)**2 and (y-ycenter)**2 lesser than radius**2
    """
    xcenter = radius
    ycenter = radius
    circle = []
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x**2 + y**2 <= radius**2:
                circle.append("*")
            else:
                circle.append(" ")
        circle.append("\n")
    return circle

#>>> print results from circle(10)
print("".join(circle(10)))


