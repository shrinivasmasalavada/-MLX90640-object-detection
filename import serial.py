import serial
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial('COM5',115200)

plt.ion()

while True:

    line = ser.readline().decode().strip()
    data = line.split(',')

    if len(data) >= 768:

        temp = np.array(data[:768],dtype=float)
        temp = temp.reshape((24,32))

        plt.clf()
        plt.imshow(temp,cmap='hot')
        plt.colorbar()
        plt.pause(0.01)