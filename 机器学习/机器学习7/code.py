# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 08:58:52 2018

@author: peter
"""

#coding:utf-8
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras.optimizers import Adam
from matplotlib import pyplot as plt


#Parameter Setting:
TIME_STEPS = 20  #same size as the height of the image
INPUT_SIZE =  1  #same size as the width of the image
BATCH_SIZE = 50
BATCH_START = 0
OUTPUT_SIZE = 1
CELL_SIZE = 50
LR = 0.01

#generate data for training:
def gen_data():
    global BATCH_START, TIME_STEPS, BATCH_SIZE
    xs = np.arange(BATCH_START, BATCH_START+TIME_STEPS*BATCH_SIZE).reshape(BATCH_SIZE, TIME_STEPS) / (1.0*np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEPS
    return [seq[:,:,np.newaxis], res[:,:,np.newaxis], xs]

    # plt.plot(xs[0,:], res[0,:], 'r', xs[0,:], seq[0, :], 'b--')
    # plt.show()
    # exit()

#build model
model = Sequential()
#Input Level
model.add(LSTM(
    output_dim = CELL_SIZE,
    batch_input_shape=(BATCH_SIZE, TIME_STEPS, INPUT_SIZE),
    return_sequences=True,  #define whether output after each training or just output after the last training
    stateful=True  #define the states between each batch, if continuous True else False
))

#Output Level
model.add(TimeDistributed(Dense(OUTPUT_SIZE)))  #If "return_sequences" setting for True, then need to add TimeDistributed()

#optimizer
adam = Adam(lr=LR)

#compile model
model.compile(optimizer=adam,
              loss='mse',
              metrics=['accuracy'])

#training model
print("~~~~Training~~~~")
for step in range(401):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch, Y_batch, xs = gen_data()
    cost = model.train_on_batch(X_batch, Y_batch)
    pred = model.predict(X_batch, BATCH_SIZE)
    plt.plot(xs[0, :], Y_batch[0].flatten(), 'r', xs[0, :], pred.flatten()[:TIME_STEPS], 'b--')
    plt.ylim((-1.2, 1.2))
    plt.draw()
    plt.pause(0.1)
    # evaluate model
    if step % 10 == 0:
        print('Evaluation step: %d: loss: %.8f \n' % (step, cost[0]))