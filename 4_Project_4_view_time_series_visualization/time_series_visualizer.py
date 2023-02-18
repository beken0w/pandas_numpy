import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates.
# Consider setting index column to 'date'.)
path = r"D:\Dev\pandas_numpy\4_Project_4_view_time_series_visualization\fcc-forum-pageviews.csv"
df = pd.read_csv(path, parse_dates=['date'], index_col='date')


# Clean data
del_amt = int((df.sort_values(by='value').count()*0.025))+1
df = df.sort_values(by='value')[del_amt:-del_amt]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(legend='', xlabel="Date", ylabel="Page Views",
                  title=r"Daily freeCodeCamp Forum Page Views 5/2016-12/2019",
                  figsize=(15, 7)).figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()
    fig = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    # fig = fig.unstack()
    # Draw bar plot
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    fig = sns.catplot(
        legend='',
        x='year', y='value', data=df_bar, hue='month', kind='bar',
        hue_order=labels, palette=sns.color_palette("Paired", 12)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(loc='upper left', title='Months')

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
    ordering = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(1, 2, 1)
    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'])
    ax1.set(xlabel="Year", ylabel="Page Views",
            title="Year-wise Box Plot (Trend)")

    ax2 = fig.add_subplot(1, 2, 2)
    sns.boxplot(data=df_box, x=df_box['month'], y=df_box['value'],
                order=ordering)
    ax2.set(xlabel="Month", ylabel="Page Views",
            title="Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
