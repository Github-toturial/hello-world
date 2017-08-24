import numpy as np
import matplotlib.pyplot as plt
import random
class autoperiod(object):
    def __init__(self, time_series = []):
        self.time_series = time_series

    def getTimeseries(self):
        return self.time_series

    def setTimeseries(self, time_series):
        self.time_series = time_series

    def FFT(self):
        a = self.time_series
        return np.fft.rfft(a)


    def getESD(self):
        a = self.FFT()
        return np.abs(a**2)


    def diagram(self, i):
        if i==0:
            a = self.getESD()
            plt.plot(np.arange(0.0, 0.5+0.0025, 0.0025), a)
            plt.show()
        if i==1:
            plt.plot(np.arange(0.0, 1.0, 0.0025), self.getTimeseries())
            plt.show()
if __name__ == '__main__':
    a = [np.sin(np.pi/25*i)+ 2*np.sin(np.pi/20*i)+0.5*np.sin(np.pi/30*i) for i in range(400)]
    testgram = autoperiod(a)
    print(testgram.FFT())
    testgram.diagram(0)