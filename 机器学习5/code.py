# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:04:43 2018

@author: peter
"""
import numpy 
X = numpy.linspace(-1,1,200)
numpy.random.shuffle(X) 
Y = 0.5*X + 2 + numpy.random.normal(0, 0.05, 200)
import keras
model = keras.models.Sequential() 
model.add(keras.layers.Dense(1,input_dim=1)) 
model.compile(loss='mse', optimizer='sgd') 
for step in range(301):
    print(model.train_on_batch(X, Y))
print(model.layers[0].get_weights())