#!/usr/bin/env python3
"""
Basic plotting script for nanofluid radiator experimental data.

This script loads the experimental results CSV and defines a function
to plot thermal effectiveness versus nanoparticle concentration.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_effectiveness_vs_concentration(data_file):
    """
    Plot heat transfer effectiveness as a function of nanoparticle concentration.

    Parameters
    ----------
    data_file : str
        Path to the CSV file containing experimental data.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The generated figure object.
    ax : matplotlib.axes.Axes
        The axes object of the plot.
    """
    # Load the data
    df = pd.read_csv(data_file)

    # Calculate effectiveness as (InletTemp - OutletTemp) / (InletTemp - AmbientTemp)
    # For simplicity, assume ambient temperature is 25°C
    ambient_temp = 25.0
    df['Effectiveness'] = (df['InletTemp_C'] - df['OutletTemp_C']) / (df['InletTemp_C'] - ambient_temp)

    # Group by concentration and compute mean effectiveness per flow rate
    fig, ax = plt.subplots(figsize=(8, 5))
    for flow_rate in df['FlowRate_L/min'].unique():
        subset = df[df['FlowRate_L/min'] == flow_rate]
        # Aggregate by concentration
        agg = subset.groupby('Concentration_percent')['Effectiveness'].mean().reset_index()
        ax.plot(agg['Concentration_percent'], agg['Effectiveness'],
                marker='o', label=f'Flow = {flow_rate} L/min')

    ax.set_xlabel('Nanoparticle Concentration (%)')
    ax.set_ylabel('Thermal Effectiveness')
    ax.set_title('Effect of Nanoparticle Concentration on Radiator Effectiveness')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

    return fig, ax


if __name__ == '__main__':
    # Example usage: plot the data from the default location
    import os
    data_path = os.path.join('..', 'data', 'experimental_results.csv')
    if os.path.exists(data_path):
        fig, ax = plot_effectiveness_vs_concentration(data_path)
        plt.tight_layout()
        plt.savefig('effectiveness_vs_concentration.png', dpi=300)
        print('Plot saved as effectiveness_vs_concentration.png')
        plt.show()
    else:
        print(f'Data file not found at {data_path}. Please adjust the path.')