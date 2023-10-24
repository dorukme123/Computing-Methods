import matplotlib.pyplot as mplt
import numpy as np

mplt.style.use('bmh');
# for jupiter
# %matplotlib inline

# x, y data points
x = np.array([0, 0.99, 2]);
y = np.array([-1, 0, 0.434]);

def divided_differences_table(x, y):
    # divided differences table

    n = len(y);
    coeff = np.zeros([n,n]) # returns new array given zeros
    # y column 1st
    coeff[:,0] = y # setting y to first column
    # for loop to set divided diff table
    for j in range(1, n):
        for i in range(n-j):
            coeff[i][j] = (coeff[i+1][j-1] - coeff[i][j-1]) / (x[i+j] - x[i])
        print(f"{j}:{coeff[i][j]}");
    return coeff
def evaluate_newton_poly(coeff, xdata, x):
    # evaluate newton polynomial
    n = len(xdata) - 1
    p = coeff[n]
    # main loop
    for i in range(1, n+1):
        p = coeff[n-i] + (x - xdata[n-i])*p
    print(f"at {x}: evaluated: {p}");
    return p

# get diveded difference coefficient
get_div_diff = divided_differences_table(x,y)[0,:];
# evaluate new data points
newx = np.arange(x[0], x[-1]+0.1, 0.1) # (start=x[0], stop=x[-1]+0.1 or as we wish, scale=(as we please)pref=0.1);
newy = evaluate_newton_poly(get_div_diff, x, newx);

mplt.figure(figsize=(8, 6), dpi=80) # 80x80
mplt.plot(x, y, 'bo')
mplt.plot(newx, newy)
mplt.show()
