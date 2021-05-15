##############################################################################
# Kütüphanelerin yüklenmesi
# Importing Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# Verilerin okunması
# Reading data from dataset

veriler = pd.read_csv("eksikveriler.csv")  # alternatively "pd.read_excel" if the dataset is an excel file
