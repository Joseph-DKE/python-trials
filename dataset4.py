from sklearn.datasets import make_circles
from matplotlib import pyplot
from pandas import DataFrame
import numpy as np
# generate 2d classification dataset
X, y = make_circles(n_samples=100, noise=0.05)
score = []
fscore = []
for i in X:
    score.append(i.item(0))
    fscore.append(i.item(1))
print(score)
print(fscore)
# scatter plot, dots colored by class value
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
colors = {0:'red', 1:'blue'}
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
pyplot.show()