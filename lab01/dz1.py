
import math
import numpy as np


# change range here:
ranges = [0,1];

# lenght of data:
data_len = len(ranges);

# f(x) value:
y = [];

# find f(x) value:
for i in range(data_len):
    number = np.abs(ranges[i])*math.sin(ranges[i]);
    y.append(number);
    
# get point of interpolation:
def get_interpolation_point(x,x2,y,y2):
    int_point = y + ((x-x2)/(x2-x)) * (y2 - y);
    return int_point;

# set point of interpolation:
ix_point = get_interpolation_point(ranges[0],ranges[1],y[0],y[1]);

# interpolated value:
iy_point = 0;

# lagrange algorith:
for i in range(data_len):
    p = 1;
    for j in range(data_len):
        if i != j:
            p = p * (ix_point - ranges[j])/(ranges[i] - ranges[j]);
    iy_point = iy_point + p * y[i];

# printout the point value:
print(f"Interpolated value at {ix_point} is {iy_point}");

