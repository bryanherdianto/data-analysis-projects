import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv');

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(20,10))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = [year for year in df['Year']]
    y1 = [slope1 * x1 + intercept1 for x1 in x1]
    ax.plot(x1, y1, color='red')
    
    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    x2 = [year for year in new_df['Year']]
    y2 = [slope2 * x2 + intercept2 for x2 in x2]
    ax.plot(x2, y2, color='green')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()