"""
Here we will test Copilot's usage of libraries in order to plot data (the imports were inserted by me, to incentivize the use of the libraries)
"""

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from matplotlib import animation

def plot_sphere (radius: float):
    """>>>
    plot a sphere in 3d proection using pyplot
    """
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = radius * np.cos(u) * np.sin(v)
    y = radius * np.sin(u) * np.sin(v)
    z = radius * np.cos(v)

    # plot the sphere
    ax = plt.subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, color="r", alpha=0.2)
    ax.scatter(0, 0, 0, color="g", s=100)
    ax.set_xlim([-1.0, 1.0])
    ax.set_ylim([-1.0, 1.0])
    ax.set_zlim([-1.0, 1.0])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

def plot_random_graph_network(n: int):
    """>>>
    Creates a random graph made up of n nodes, connected randomly and displays them using pyplot. Each node is represented as circle, and each node's edges are represented as straight lines
    """
    G = nx.gnm_random_graph(n, n*(n-1)/2)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='r', alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    plt.axis('off')
    plt.show()

def plot_geometric_brownian_motion (points: int, up_to: float):
    """>>>
    Plots a line plot of a geometric brownian motion. points defines the number of points to plot and "up_to" defines the max x x value to plot. Y axis is in logartihmic scale
    """
    t = np.linspace(0, up_to, points)
    log_S = np.log(100) * np.cumsum(np.random.standard_normal(points))
    plt.plot(t, log_S)
    plt.xlabel("t")
    plt.ylabel("log_S")
    plt.show()

def plot_sine_wave_with_frequencies (frequencies: list):
    """>>>
    plots a single waveform that corresponds to the addition of sinewaves of each of the frequencies supplied in the "frequencies" list. X axis corresponds to 4*(1/min(frequencies)).
    """
    x = np.linspace(0, 4*(1/min(frequencies)), 1000)
    y = 0
    for f in frequencies:
        y += np.sin(f * x * (2*np.pi))
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
def plot_area_under_the_curve(x: list, y: list):
    """>>>
    Creates a plot of the area under the curve of the supplied x,y graph. y and x must have matching lengths.
    The area under the curve is greyed out.
    """
    area = 0
    for i in range(len(x)-1):
        area += (y[i+1] + y[i]) / 2 * (x[i+1] - x[i])
    plt.plot(x, y)
    plt.fill_between(x, y, color='grey', alpha=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    print("The area under the curve is: " + str(area))

def plot_animated_sine_wave():
    """>>>
    Plots a sine wave that is animated.
    """
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2*np.pi), ylim=(-1.5, 1.5))
    line, = ax.plot([], [], lw=2)
    def init():
        line.set_data([], [])
        return line,
    def animate(i):
        x = np.linspace(0, 2*np.pi, 1000)
        y = np.sin(x + i/10.0)
        line.set_data(x, y)
        return line,
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
    plt.show()

def scatter_animated_custom (xx:list, yy:list, fps = 10):
    """>>>
    Gradually iterates through points in a scatter plot. Each frame iterates a single x,y point, such that only one point is visible at any time. The plot window should be adjusted to the size of xx and yy.
    """
    fig = plt.figure()
    ax = plt.axes(xlim=(min(xx), max(xx)), ylim=(min(yy), max(yy)))
    scat = ax.scatter(xx, yy)
    def animate(i):
        scat.set_offsets([xx[i], yy[i]])
        return scat,
    anim = animation.FuncAnimation(fig, animate, frames=len(xx), interval=1000/fps, blit=True)
    plt.show()


#>>> run this if this is main
if __name__ == "__main__":
    #>>> test plot_sphere
    plot_sphere(1.0)

    #>>> test plot_random_graph_network
    plot_random_graph_network(10)

    #>>> test plot_geometric_brownian_motion
    plot_geometric_brownian_motion(100, 10.0)

    #>>> test plot_sine_wave_with_frequencies using 10 frequencies
    plot_sine_wave_with_frequencies([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

    #>>> create x axis with 100 points from 0 to 1
    x = np.linspace(0, 1, 100)
    #>>> create y axis a sine wave with a frequency of 0.5
    y = np.sin(0.5 * x * (2*np.pi))
    #>>> test plot_area_under_the_curve
    plot_area_under_the_curve(x, y)
    #>>> calculate the integral of the area under the curve using the trapazoidal rule
    area = np.trapz(y, x)
    #>>> print the area
    print("The area under the curve is: " + str(area))

    #>>> test plot_animated_sine_wave
    plot_animated_sine_wave()

    #>>> create x axis with 100 points from 0 to 1
    x = np.linspace(0, 1, 100)
    #>>> create y axis as a decreasing sine wave
    y = np.sin(x * (2*np.pi))
    #>>> test scatter_animated_custom using 60 fps
    scatter_animated_custom(x, y, fps=60)

