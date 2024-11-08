import numpy as np
import pandas as pd


def get_data() :
    df = pd.read_csv("auto-mpg.csv")
    df.origin = df.origin.map({1 : "USA", 2 : "Germany", 3 : "Japan"})
    df = df.loc[df.horsepower.str.isdigit(), ['origin', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'mpg']]
    df.horsepower = df.horsepower.astype(int)
    return df
