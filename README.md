# Monte Carlo Simulation to Approximate Pi
This Python code implements a Monte Carlo simulation to approximate the value of pi.

The simulation generates random points within a square of length 1 and counts the number of points that fall within a circle of radius 0.5 and centered at the midpoint of the square. The ratio of points inside the circle to the total number of points generated provides an estimate of the area of the circle. Since the area of the circle is pi/4, multiplying the estimate by 4 provides an estimate of pi.
Dependencies

    numpy
    matplotlib

How to Use

The MonteCarloSimulation class takes two parameters:

    n_runs - the number of random points to generate for the simulation
    early_stop (optional) - the number of iterations to plot before stopping early. Default is 1000.

To run the simulation and obtain an estimate of pi, create an instance of the MonteCarloSimulation class with a desired value for n_runs. Then, call the run method with an optional plot parameter to visualize the simulation results. The run method returns an estimate of pi.

Example usage:

python

sim = MonteCarloSimulation(1000000)
pi = sim.run(plot=True)
print(f"pi: {pi}")

This generates 1 million random points and plots the first 1000 points that fall within the circle. The final estimate of pi is printed to the console.
