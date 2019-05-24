#!/usr/local/bin/python2.7
# _*_ coding: utf-8 _*_
# file: test.py
# time: 2018/7/1 下午5:05
# version: 1.0
# __author__: ChengChen
# contact: saicc4869@163.com
from Functions.WiFiArrMUSICAnalysis import *
import matplotlib.pyplot as plt
from sklearn.neighbors import kde
from pyqtgraph.Qt import QtWidgets, QtCore
import pyqtgraph as pg


""" 
read from a existed binary file
"""
csi_trace = IntelDeviceService(Intel_IWL5300_API());
csi_trace.open('data/20m-25-1.dat')

MUSIC = WiFi_MUSIC_API(csi_trace)

degList = MUSIC.csi_facto_aoa()

fig = plt.figure('Kernel Density Estimate')
X_plot = np.arange(-90, 91, 1)[:, np.newaxis]
kde = kde.KernelDensity(kernel='gaussian', bandwidth=1).fit(degList)
log_dens = kde.score_samples(X_plot)
plt.plot(X_plot[:, 0], np.exp(log_dens), '-')
plt.show()

