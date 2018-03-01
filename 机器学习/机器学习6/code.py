# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 13:14:52 2018

@author: peter
"""

# -*- coding: utf-8 -*-
#coding:utf-8
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.datasets import mnist
from PIL import Image
(x_train, y_train), (x_test, y_test) = mnist.load_data()  #loading the data source

# print len(x_train), len(y_train), len(x_test), len(y_test)
# X shape = (60000, 28, 28), y shape = (60000, 1)

# for pic in range(10):    #I change the first 10 digital numbers into pictures like the attachments
#     img = [0]*28
#     for i in range(28):
#         img[i] = list(X_train[pic][i])
#
#     print img
#
#     new = Image.new('L',(28,28),0)
#     for i in range(28):
#         for j in range(28):
#             new.putpixel((i,j),int(img[j][i]) % 256)
#     new.save('%s.png' % pic)

#data processing:
#print x_train.shape, x_test.shape
# (60000, 28, 28) , (10000, 28, 28)

X_train = x_train.reshape(60000,784) / 255.0
X_test = x_test.reshape(10000,784) / 255.0
Y_train = np.array([[0]*10 for i in range(60000)])
for i in range(60000):
    Y_train[i][y_train[i]] = 1
Y_test = np.array([[0]*10 for i in range(10000)])
for i in range(10000):
    Y_test[i][y_test[i]] = 1

#build model
model = Sequential()
#Level 1
model.add(Dense(256, input_dim = 784))  # input 784 dimension --> output 256 dimension
model.add(Activation('relu'))  #https://www.zhihu.com/question/29021768 "for relu activation function"
#Level 2
model.add(Dense(10)) #Level 2 no need input_dim, input 256 dimension --> output 10 dimension
model.add(Activation('softmax'))  # softmax activation function for classify combined with loss:categorical_crossentropy for multiple classification

#optimizer
rmsprop = RMSprop(lr = 0.001, rho=0.9, epsilon=1e-8, decay=0.0)

#compile model
model.compile(optimizer=rmsprop, loss='categorical_crossentropy',
              metrics=['accuracy'])

#training model
print("~~~~Training~~~~")
model.fit(X_train, Y_train, epochs=2, batch_size=32) #training 2 times with batch size 32

#evaluate model
print("~~~~Evaluation~~~~")
loss, accuracy = model.evaluate(X_test, Y_test, batch_size=32, verbose=1)
print('\nloss: %f, accuracy: %f' % (loss, accuracy))