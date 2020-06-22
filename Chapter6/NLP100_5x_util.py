import numpy as np
import pandas as pd
import pickle
from NLP100_54 import accuracy
from NLP100_52 import learn

DATA_EXTENSION = '.txt'
FEATURE_EXTENSION = '.feature.txt'
LABEL_EXTENSION = '.label.txt'

# b = business, t = science and technology, e = entertainment, m = health
CATEGORY_NAMES = ['business', 'entertainment', 'health', 'science and technology']

def load_clf(pickle_fname):
    with open(pickle_fname, mode='rb') as fp:
        clf = pickle.load(fp)
    return clf

def load_features(fname):
    """ load feature from file

    Args:
        fname (str): file name without extension

    Returns:
        DataFrame: Feature DataFrame
    """
    feature_df = pd.read_csv(feature_file_path(fname))
    return feature_df

def load_labels(fname):
    """ Load labels from file

    Args:
        fname (str): file name without extension

    Returns:
        DataSeries: Label DataSeries
    """
    label_ds = pd.read_csv(label_file_path(fname), header=None)[0]
    return label_ds

def load_feature_names(fname):
    feature_df = load_features(fname)
    return feature_df.columns

def data_file_path(fname):
    return fname + DATA_EXTENSION

def feature_file_path(fname):
    return fname + FEATURE_EXTENSION

def label_file_path(fname):
    return fname + LABEL_EXTENSION