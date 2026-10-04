import pickle
import random

from sklearn.datasets import fetch_openml
from numpy import argmax, sqrt
from ai import *
from myPygame import myPygame

with open("net.pkl", "rb") as f:
    net = pickle.load(f)

X, y = fetch_openml("mnist_784", version=1, as_frame=False, return_X_y=True)

X=X[:1000]

sampleX=X[0]

screen=myPygame(sampleX, 10)




while True:
    index=random.randint(0, len(X)-1)
    frame = X[index]
    targ = y[index]
    n, net = netInput(net, frame)

    output = argmax(n)

    print(f"output: {output}, target: {targ}")

    screen.update(frame)
    if output == int(targ):
        continue

    while not screen.buttonPressed():
        screen.FPSCLOCK.tick(60)
