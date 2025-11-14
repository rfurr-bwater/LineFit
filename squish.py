import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("data.csv", delimiter=",", dtype=str,skiprows=1)

x = data[:,0].astype(np.float32)
y = data[:,1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)

slope = params[0].round(2)
intercept = params[1].round(2)

### EXERCISE 1
print_equation(slope,intercept,"grams","milimeters")

### EXCERICE 2
plt.figure()
plt.scatter(x,y,label="Data")
plt.plot(x,linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("Mass (grams)") #change the units as appropriate
plt.ylabel("Height (milimeters)")  #change the units as appropriate
plt.show()