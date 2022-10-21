import matplotlib.pyplot as plt
import csv
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

def readCSV (path):
  data = []
  header = [] # removes first line of file
  filename = path
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # removes first line of file
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
  return data


  