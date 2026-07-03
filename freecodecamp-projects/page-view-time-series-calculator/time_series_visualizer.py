import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
filter = (df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))
df = df[filter]

def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(20,10))
    plt.plot(df.index, df.values, color='green')
    plt.ylabel('Page Views')
    plt.xlabel('Date')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    data_bar = df.groupby(['year', 'month'], sort=False).mean()
    bar_plot = pd.DataFrame(data_bar)
    bar_plot.rename(columns={0:'views'}, inplace=True)
    bar_plot = bar_plot.reset_index()
  
    lost_data = {
        'year': ['2016', '2016', '2016', '2016'],
        'month': ['January', 'February', 'March', 'April'],
        'value': [0, 0, 0, 0]
    }
  
    final = pd.concat([pd.DataFrame(lost_data), bar_plot])
    final.rename(columns={'year':'Years','month':'Months','value':'Average Page Views'}, inplace=True)

    # Draw bar plot
    plt.figure(figsize=(10,15))
    sns.barplot(data=final, x='Years', y='Average Page Views', hue='Months', palette='prism')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=100)

    sns.boxplot(data=df_box, x='year', y='value', hue='year', palette='icefire', ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
  
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', hue='month', order=order, ax=ax[1], palette='Dark2')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
