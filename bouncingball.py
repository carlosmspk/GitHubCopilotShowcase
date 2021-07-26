"""
This program will simulate a bouncing ball, given initial position and velocity. The result will be printed as a plot in x and y
"""

import matplotlib.pyplot as plt

def simulate_bouncing_ball (x0, y0, vx0, vy0, steps, dt, coefficient_of_restitution = 0.2, g = 9.83) -> list:
    """>>>
    Simulate the bouncing ball. Gravity affects the y coordinate only. When it its the floor on the y axis, it bounces back
    :param x0: initial x position
    :param y0: initial y position
    :param vx0: initial x velocity
    :param vy0: initial y velocity
    :param steps: number of steps
    :param dt: time step
    :param g: gravity constant
    :param coefficient_of_restitution: coefficient of restitution of each bounce
    :return: list of positions
    """
    x_positions = [x0]
    y_positions = [y0]
    vx = vx0
    vy = vy0
    for i in range(steps):
        x_positions.append(x_positions[-1] + vx * dt)
        y_positions.append(y_positions[-1] + vy * dt)
        if y_positions[-1] < 0:
            vy = -vy * coefficient_of_restitution
            y_positions[-1] = 0
        else:
            y_positions[-1] = y_positions[-1] + vy * dt
            vy = vy - g * dt
    return x_positions, y_positions

#>>> set initial x and y positions to 1.0
x0 = 1.0
y0 = 1.0
#>>> set initial x and y velocities to 1.0
x0 = 1.0
y0 = 1.0
#>>> set number of time steps to 250
steps = 250
# set time step
dt = 0.01
#>>> set coefficient of restitution to 0.8
coefficient_of_restitution = 0.8
# set gravity constant
g = 9.8

#>>> test function
x_positions, y_positions = simulate_bouncing_ball(x0, y0, x0, y0, steps, dt, coefficient_of_restitution, g)
plt.plot(x_positions, y_positions)
plt.show()