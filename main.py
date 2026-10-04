import pickle

from sklearn.datasets import fetch_openml
from numpy import argmax
from ai import *


try:
    with open("net.pkl", "rb") as f:
        net = pickle.load(f)
except:
    with open("net.pkl", "wb") as f:
        pickle.dump(genNewNet(), f)

with open("net.pkl", "rb") as f:
    net = pickle.load(f)



X, y = fetch_openml("mnist_784", version=1, as_frame=False, return_X_y=True)

X=X[1000:]
y=y[1000:]

emptys=[0 for _ in range(10)]
while True:
    right = 0
    for i in range(1000):
        index=random.randint(0, len(X)-1)
        frame = X[index]
        targ = y[index]
        n, net = netInput(net, frame)

        output = argmax(n)

        if output == int(targ):
            right += 1
        
        shouldHaveBeen = emptys.copy()

        shouldHaveBeen[int(targ)]=1
        net.train(shouldHaveBeen)

    with open("net.pkl", "wb") as f:
        pickle.dump(net, f)

    print(f"right: {right} out of 1000, {right/10}%")