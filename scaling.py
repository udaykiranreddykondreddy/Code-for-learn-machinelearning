#!/usr/bin/python3

"@Author: AnuragAnalog"
"Python code for Data-Scaling(1D and 2D arrays)"

import sys
import numpy as np
import pandas as pd

class scaling():
    """
        A Class which contains some of the popular scaling methods.
    """
    def checkna(self, data: [np.array, list]) -> None:
        """
            Checks whether data contains NA or nan values or not.
        """
        nele = np.prod(np.shape(data))
        if any(pd.isna(np.reshape(data, (nele, 1)))):
            print("Data contains NA or nan values")
            print("Give the data which is NA or nan free")
            sys.exit()

    def standerdization(self, data: [np.array, list]) -> np.array:
        """
            It is a scaling technique which scales the data such that it's mean
            zero and standerd deviation is one.
        """
        data = np.array(data)
        self.checkna(data)

        shape = np.shape(data)
        if len(shape) == 1:
            data = (data - np.mean(data))/np.std(data)
        elif len(shape) == 2:
            for i in range(shape[-1]):
                mu = np.mean(data[:, i])
                sigma = np.std(data[:, i])
                data[:,i] = (data[:,i] - mu)/sigma
        else:
            print("This is only upto two-dimensional data")
        return data

    def normalization(self, data: [np.array, list]) -> np.array:
        """
            The values of the data are scaled to the interval [-1, 1] with a
            mean of zero.
        """
        data = np.array(data)
        self.checkna(data)

        shape = np.shape(data)
        if len(shape) == 1:
            data = (data - np.mean(data))/(max(data)-min(data))
        elif len(shape) == 2:
            for i in range(shape[-1]):
                mu = np.mean(data[:, i])
                maxi = max(data[:, i])
                mini = min(data[:, i])
                data[:,i] = (data[:,i] - mu)/(maxi - mini)
        else:
            print("This is only upto two-dimensional data")
        return data

    def minmax_scaling(self, data: [np.array, list]) -> np.array:
        """
            The values of the data are scaled to the interval [0, 1].
        """
        data = np.array(data)
        self.checkna(data)

        shape = np.shape(data)
        if len(shape) == 1:
            data = (data - min(data))/(max(data)-min(data))
        elif len(shape) == 2:
            for i in range(shape[-1]):
                mini = min(data[:, i])
                maxi = max(data[:, i])
                data[:,i] = (data[:,i] - mini)/(maxi - mini)
        else:
            print("This is only upto two-dimensional data")
        return data

if __name__ == '__main__':
    """
        This code is only for testing and validation of methods
    """
    data = [3, 2, np.nan, 4]
    data1 = [3, 4, 12, 20]
    data2 = np.array([2,3,1,24,5,2])

    std = scaling()
    print(std.standerdization(data1))
    print(std.standerdization([[3, 4],[12, 20]]))
    print(std.minmax_scaling(data2))
    print(std.normalization(data))
