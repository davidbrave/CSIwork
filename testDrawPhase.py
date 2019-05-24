# -*- coding: utf-8 -*-
"""
Created on Fri May 24 2019

@author: David
"""

from Functions.WiFiArrMUSICAnalysis import *
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.neighbors import kde
from pyqtgraph.Qt import QtWidgets, QtCore
import pyqtgraph as pg

""" 
read from a existed binary file
"""
csi_trace = IntelDeviceService(Intel_IWL5300_API());
csi_trace.draw_phase('data/20m-0-1.dat')



