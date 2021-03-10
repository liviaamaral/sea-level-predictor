import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  # Create scatter plot
  plt.scatter(x, y)

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(x, y)
  year_range = list(range(1880, 2050, 1))
  best_fit = [intercept + slope * i for i in year_range]
  plt.plot(year_range, best_fit)

  df_2 = df.loc[df["Year"] >= 2000]
  x = df_2['Year']
  y = df_2['CSIRO Adjusted Sea Level']

  # Create second line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(x, y)
  year_range_2 = list(range(2000, 2050, 1))
  best_fit_2 = [intercept + slope * i for i in year_range_2]
  plt.plot(year_range_2, best_fit_2)

  # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")

    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()