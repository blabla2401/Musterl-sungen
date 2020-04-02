import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

if __name__ == "__main__":

  #import data
  data = pd.read_csv("/home/usr/challenge/data.csv", header = None, index_cols = None)
  data = np.asarray(data)

  x_data = data[0,:]
  y_data = data[1,:]
  y_err = data[2,:]

  #plot
  plt.plot(x_data,y_data, label= "plot")
  
  # curve fit
  def func(x,a,b,c):
    return a*x**2 + b*x +c
  popt,pcov = curve_fit(x_data,y_data,sigma = y_err)
  
  #plot solution
  plt.plot(x_data,func(x_data, *popt), label="Lösung")
  
  print("a=", popt[0][0] +r"\pm"+pcov[0][0])
