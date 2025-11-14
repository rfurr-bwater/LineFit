import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("data.csv", delimiter=",", dtype=str,skiprows=1)

x = data[:,0].astype(np.float32)
y = data[:,1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)

slope = params[0]
intercept = params[1]