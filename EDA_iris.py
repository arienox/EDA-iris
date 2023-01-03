# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:31:01 2022

@author: ASUS
"""

#basic EDA, , 
import pandas as pd
import numpy as np
#import os
import seaborn as sns
import matplotlib.pyplot as plt


#os.chdir("path")
iris = pd.read_csv('Iris.csv')
print(iris.head())
print(iris.describe())
sns.countplot(x='Species', data=iris)
sns.scattterplot('SepalLengthCm','SepalWidthCm', hue='Species',data=iris)
sns.pairplot(iris.drop(['Id'], axis =1),hue='Species',height=2)
#sns.boxenplot()
x=iris.corr(method='pearson')
print(x)
sns.heatmap(iris.corr_matrix,method='pearson'.drop(['Id'],axis=1).drop(['Id'],axis=0))
plt.boxplot('SepalWidthCm', data=iris)


plt.show()


#cd python3 bin
#python -n pip install seaborn
#pip install seaborn