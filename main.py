import numpy as np
import matplotlib.pyplot as plt

class MonteCarloSimulation:
    def __init__(self, n_runs, early_stop=1000):
        self.n = n_runs
        self.early_stop = early_stop
        
    def run(self, plot=False):
        pts = self.get_random_points(n=self.n)
        results = self.are_in_circle(points=pts)
        pi = self.get_pi(pts=pts, results=results)
        if plot:
            self.plot_simulation(pts=pts, results=results, 
                                 pi=pi, early_stop=self.early_stop)
        return pi
        
    def get_random_points(self, n):
        return np.random.random((n, 2))
    
    
    def are_in_circle(self, points):
        matrix = points - [0.5, 0.5]
        dist = np.linalg.norm(matrix, axis=1)
        return dist <= 0.5
    
    def get_pi(self, pts, results):
        return (np.count_nonzero(results) / len(pts))*4
        
    def plot_simulation(self, pts, results, pi, early_stop):
        figure, axes = plt.subplots() 
        cc = plt.Circle(( 0.5 , 0.5 ), 0.5 ) 
        cc.set_fill(False)
         
        axes.set_aspect( 1 ) 
        axes.add_artist( cc ) 
        for i, pt in enumerate(pts):
            if i == self.early_stop:
                print(f"Stoped plotting early at i={i}")
                break
            elif results[i]:
                plt.scatter(pt[0], pt[1], color="green")
            else:
                plt.scatter(pt[0], pt[1], color="red")
        plt.scatter(0.5, 0.5, color="black")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.title(f"Monte Carlo Simulation of pi using n={round(len(pts)/1000000, 2)} Million points,\nyields pi={pi}") 
        plt.show()


if __name__ == "__main__":
    sim = MonteCarloSimulation(1000000)
    pi = sim.run(plot=True)
    print(f"pi: {pi}")
