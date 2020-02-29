from vpython import *
import numpy as np
import time

G = 6.67408e-11 # Gravitational constant: meters^3/(kg*sec^2)

def load_universe(filename):
    """
    A method to load in a set of point masses whose dynamics
    are to be simulated
    Parameters
    ----------
    filename: string
        Path to file holding a different point mass on each line
        Each line should hold
        px, py, pz, vx, vy, vz, mass, color_r, color_b, color_g, size
        Where (px, py, pz) is the initial position
        and (vx, vy, vz is the mass)

    Returns
    -------
    P: ndarray(N, 3)
        An array of the initial positions of all masses, with
        one xyz position per row, and each coordinate in meters
    V: ndarray(N, 3)
        An array of the initial velocities of all masses,
        with one xyz velocity per row, with each coordinate
        in meters/second
    masses: ndarray(N)
        An array of the masses of each body in kilograms
    colors: ndarray(N, 3)
        An array of RGB color coordinates for each body
    sizes: ndarray(N)
        The radius of the sphere to draw (not necessarily to scale,
        but so that everything shows up while rendering)
    """
    X = np.loadtxt(filename, delimiter=',')
    # First three columns are xyz coordinates of initial position
    P = X[:, 0:3]
    # Next three columns are xyz coordinates of initial velocity
    V = X[:, 3:6]
    # Next column is the mass
    masses = X[:, 6]
    # Next three columns are the color
    colors = X[:, 7:10]
    # Last column is the size to draw (not necessarily the actual size of the planet)
    sizes = X[:, -1]
    return P, V, masses, colors, sizes

## First, load in the universe an set up all of the spheres
## in vpython
P, V, masses, colors, sizes = load_universe("4Planets.csv")
N = P.shape[0] # Store away how many bodies there are
spheres = []
for i in range(N):
    c = colors[i, :]
    ball = sphere(pos=vector(P[i, 0], P[i, 1], P[i, 2]), radius=sizes[i], color=vector(c[0], c[1], c[2]), make_trail=True)
    spheres.append(ball)

SECONDS_IN_DAY = 3600*24
# Every second in the simulation is about a month
speedup_fac = SECONDS_IN_DAY*30

tic = time.time()
total_time = 0
# This text will store the elapsed time
T = wtext(text='')

# Go for 687 days, which should be the length of Mars's orbit
while total_time < SECONDS_IN_DAY*687:
    ## Step 1: Figure out the elapsed time, noting that
    ## we're speeding up the animation by some factor
    toc = time.time()
    dt = (toc-tic)*speedup_fac
    total_time += dt
    tic = toc
    T.text = "\nElapsed Time: %.3g Days"%(total_time/SECONDS_IN_DAY)

    ## Step 2: Apply physics
    ## Step 2a: Compute the acceleration for each planet
    A = np.zeros((N, 3))
    ## TODO: Fill in each row of the A matrix with the 
    ## acceleration for each body

    ## Step 2b: Apply the laws of physics to each body
    ## TODO: Update each row of V and each row of P
    ## to store the new velocity and position, respectively,
    ## of each body
    
    ## Step 3: Update graphics
    for i in range(N):
        spheres[i].pos = vector(P[i, 0], P[i, 1], P[i, 2])
    time.sleep(0.01)