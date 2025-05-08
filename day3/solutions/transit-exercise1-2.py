%matplotlib inline
import matplotlib.pyplot as plt

def plot_data(time, flux):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(time, flux)
    ax.set_xlabel('time')
    ax.set_ylabel('relative flux')
    return ax
    
ax = plot_data(time, flux)
