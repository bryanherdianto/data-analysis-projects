import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (bmi > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize(val):
  if val > 1:
      return 1
  elif val == 1:
      return 0

df['cholesterol'] = df['cholesterol'].apply(normalize)
df['gluc'] = df['gluc'].apply(normalize)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).value_counts().reset_index()
    # the function size() and value_counts() is the same
    df_cat.rename(columns={0: 'total'}, inplace=True)
    
    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')

    # Get the figure for the output
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat, dtype=int))

    # Draw the heatmap with 'sns.heatmap()'
    graph = sns.heatmap(corr, mask=mask, linewidths=.5, cmap='rocket', vmin=-0.08, vmax=0.24, annot=True, fmt="0.1f", annot_kws={"fontsize":8})
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
