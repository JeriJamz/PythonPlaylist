import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.2,2.1,3.3],#everyone guest. Arrays (3x3)
                      [-1.2,7.8,-6.1],#anyvalue 2.1<= 0
                      [7.3,-9.9,-4.5]])




#binarized data
#preprocessing.Binarizer().transform()
data_binize = preprocessing.Binarizer(threshold = 2.1).transform(input_data)#i might like this. I wanna make a compiler just for A.I use

print("\nBinarized data: \n", data_binize)
#gonna try and print SD and avg

#print mean and standard deviation
print("\nBfefore:")
print(", mean = ", input_data.mean(axis=0))
print("Srd devation = ", input_data.std(axis=0))
#add this to the preprocecssor to remove the mean
data_scaled = preprocessing.scale(input_data)
print("\nAfter:")
print("mean = ", data_scaled.mean(axis = 0))
print("Std devation = ", data_scaled.std(axis=0),'\n')
#min max
data_scaler_MinMax = preprocessing.MinMaxScaler(feature_range = (0,1))
data_scaled_MinMax = data_scaler_MinMax.fit_transform(input_data)
print("\nMin Max scaled data:\n", data_scaled_MinMax)

