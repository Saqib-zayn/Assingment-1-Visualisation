"""
Created on Tue Mar  5 15:32:16 2024

@author: saqib
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create a dataframe using pandas
un_df = pd.read_csv("Unemployment_ethnicity.csv")

# divide each column other than year by 1000, for readability
for col in un_df.columns[1:]:
    un_df[col] /= 1000
un_df.to_csv("data_divided.csv", index=False)

plt.ion()

# 1.lineplot with multiple lines.
def create_line_plot(un_df, title, filename):
    """Creates a line plot with multiple lines for each ethnicity."""
    plt.figure(figsize=(12, 6))
    for col in un_df.columns[1:]:
        plt.plot(un_df["Year"], un_df[col], label=col)
    plt.xlabel("Year")
    plt.ylabel("Number of Unemployed (in 1000s)")
    plt.title(title)
    plt.legend()
    plt.xlim(2005, 2022)
    plt.ylim(0, 2500)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


create_line_plot(
    un_df.copy(), "Number of Unemployed People By Ethnicity, By Year", "LinePlot.png")

#2.second Graph (bar chart)
def create_bar_chart(un_df, year, title, filename):
    """Creates a bar chart for unemployment rates by ethnicity in a specific year."""
    un_df_year = un_df[un_df["Year"] == year]
    ethnicities = un_df_year.columns[1:]
    unemployment_rates = un_df_year.iloc[0, 1:]
    plt.figure(figsize=(8, 6))
    plt.bar(ethnicities, unemployment_rates, color="#A3D4EE")
    plt.xlabel("Ethnicity")
    plt.ylabel("Unemployment Rate (in 1000s)")
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


create_bar_chart(un_df.copy(), 2012,
                 "Unemployment Rate by Ethnicity in 2012", "BarChart_2012.png")

#3.third Graph (pie chart)


def create_pie_charts(un_df_2019, un_df_2020, filename):
    """Creates pie charts for unemployment distribution in 2019 and 2020."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    total_unemployment_2019 = un_df_2019.iloc[0, 1:].sum()
    total_unemployment_2020 = un_df_2020.iloc[0, 1:].sum()
    percentages_2019 = [(val / total_unemployment_2019) *
                        100 for val in un_df_2019.iloc[0, 1:]]
    percentages_2020 = [(val / total_unemployment_2020) *
                        100 for val in un_df_2020.iloc[0, 1:]]
    ax1.pie(percentages_2019,
            labels=un_df_2019.columns[1:], autopct="%1.1f%%", startangle=140)
    ax1.set_title("2019")
    ax1.axis("equal")
    ax2.pie(percentages_2020,
            labels=un_df_2020.columns[1:], autopct="%1.1f%%", startangle=140)
    ax2.set_title("2020")
    ax2.axis("equal")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


create_pie_charts(un_df[un_df["Year"] == 2019],
                  un_df[un_df["Year"] == 2020], "PieCharts_2019_2020.png")
