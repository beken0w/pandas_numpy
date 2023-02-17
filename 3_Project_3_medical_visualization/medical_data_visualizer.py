import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
path = r"D:\Dev\freecodecamp-intro-to-pandas\3_Project_3_medical_visualization\medical_examination.csv"
df = pd.read_csv(path)


# Add 'overweight' column
overweight_col = df['weight'] / ((df['height'] / 100)**2)
overweight_col = overweight_col.to_frame()
overweight_col.columns = ['index']
overweight_col.loc[overweight_col['index'] <= 25, 'index'] = 0
overweight_col.loc[overweight_col['index'] > 25, 'index'] = 1
df['overweight'] = overweight_col

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values 
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=[
        'active','alco','cholesterol','gluc','overweight','smoke'])



    # Group and reformat the data to split it by 'cardio'. Show the counts of
    #  each feature. You will have to rename one of the columns for 
    # the catplot to work correctly.
    fig = sns.catplot(df_cat, x='variable', hue='value', col='cardio', kind='count')
    fig.set(ylabel='total')
    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    # Do not modify the next two lines
    fig = fig.fig
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask1 = df['ap_lo'] <= df['ap_hi']

    mask2 = df['height'] >= df['height'].quantile(0.025)
    mask3 = df['height'] <= df['height'].quantile(0.975)

    mask4 = df['weight'] >= df['weight'].quantile(0.025)
    mask5 = df['weight'] <= df['weight'].quantile(0.975)

    df_heat = df[mask1 & mask2 & mask3 & mask4 & mask5]
    # Calculate the correlation matrix
    corr = df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
