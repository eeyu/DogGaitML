# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:38:40 2021

@author: Evan Yu
"""
import numpy as np;
from abc import ABC, abstractmethod
from dataclasses import dataclass
import matplotlib.pyplot as mpl;
from CostEvaluator import CostEvaluator
from mpl_toolkits.mplot3d import Axes3D
from Optimizer import GradientDescentOptimizer, OptimizationParameters

class ParabolicCostEvaluator(CostEvaluator):
    def __init__(self, a, b):
        self.a = a;
        self.b = b
        
    def getCost(self, value):
        x = value[0];
        return (self.a * x * x + self.b * x)
    
class ParaboloidCostEvaluator(CostEvaluator):
    def __init__(self, a, b):
        self.a = a;
        self.b = b
        
    def getCost(self, value):
        x = value[0];
        y = value[1];
        return (self.a * x * x + self.b * y * y)
    
    
def optimizeParabola() :
    optimizationParameters = OptimizationParameters(0.5, 0.5, 0.9, 3);
    initialValue = np.array([5.0]);
    costEvaluator = ParabolicCostEvaluator(1.0, 0);
    optimizer = GradientDescentOptimizer(initialValue, costEvaluator, optimizationParameters);
    optimizer.optimizeUntilMaxCount(100, 0.0);
    history = optimizer.getFullHistory();
    
    count = len(history);
    xval = [];
    yval = [];
    for i in range(count):
        x = history[i][0];
        xval.append(x[0])
        yval.append(history[i][1])
    
    mpl.plot(xval, yval);
    print(xval[-1])
    
def optimizeParabaloid():
    a = 1.0
    b = 1.0
    optimizationParameters = OptimizationParameters(0.1, 0.001, 0.95, 10);
    initialValue = np.array([5.0, 5.0]);
    costEvaluator = ParaboloidCostEvaluator(a, b);
    optimizer = GradientDescentOptimizer(initialValue, costEvaluator, optimizationParameters);
    optimizer.optimizeUntilMaxCount(1000, 0.0);
    valueHistory, costHistory = optimizer.getFullHistory();
    
    count = len(costHistory);
    xval = valueHistory[:,0];
    yval = valueHistory[:,1];
    zval = costHistory;
    
    fig = mpl.figure()
    ax = fig.add_subplot(111, projection='3d')
    plotParaboloic(ax, a, b)
    ax.plot(xval, yval, zval);
    print(zval[-1]) 
    print(xval[-1])
    print(yval[-1])
    
def plotParaboloic(ax, a, b):
    x = np.linspace(0,5,20);
    y = np.linspace(0,5,20);
    x, y = np.meshgrid(x, y);
    z = a * x * x + b * y * y;
    ax.plot_surface(x, y, z, alpha=0.4);
    
def main():
    optimizeParabaloid()
    
    
if __name__ == "__main__":
    main()