"""SaveData.py: Saves data in various formats"""


# External Imports
import pandas as pd
import numpy as np

# Function to save data in CSV format


def saveCSV(data, filename):
    data.to_csv(f'savedData/{filename}.csv')

# Function to save Numpy data as .npy files


def saveNumpy(data, filename):
    np.save(f'savedData/{filename}.npy', data)
