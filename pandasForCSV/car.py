import fnmatch

import math

from IPython import display

from matplotlib import cm

from matplotlib import gridspec

from matplotlib import pyplot as plt

import numpy as np

import pandas as pd

from sklearn import metrics

import tensorflow as tf

from tensorflow.python.data import Dataset

cols = ['symboling', 'losses', 'make', 'fuel-type', 'aspiration', 'num-doors',

        'body-style', 'drive-wheels', 'engine-location', 'wheel-base',

        'length', 'width', 'height', 'weight', 'engine-type', 'num-cylinders',

        'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio',

        'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']

car_data = pd.read_csv('https://storage.googleapis.com/ml_universities/cars_dataset/cars_data.csv',sep=',', names=cols, header=None, encoding='latin-1')

car_data = car_data.reindex(np.random.permutation(car_data.index))

car_data['price'] = pd.to_numeric(car_data['price'], errors='coerce')

car_data['horsepower'] = pd.to_numeric(car_data['horsepower'], errors='coerce')

car_data['peak-rpm'] = pd.to_numeric(car_data['peak-rpm'], errors='coerce')

car_data['city-mpg'] = pd.to_numeric(car_data['city-mpg'], errors='coerce')

car_data['highway-mpg'] = pd.to_numeric(car_data['highway-mpg'], errors='coerce')

car_data['losses'] = pd.to_numeric(car_data['losses'], errors='coerce')