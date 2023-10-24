

def du (x,y):
    return 2*x*y


def euler(x_0,y_0,x_k,n_1):

    h= (x_k-x_0) /n_1
    
    for i in range (0,n_1):
        y1=y_0+h*du (x_0,y_0)
        x1=x_0+h
        x_0=x1
        y_0=y1
    
    return y1

def rutte(x_0,y_0,x_k,n_1):
    
    h= (x_k-x_0) /n_1
    
    for i in range (0,n_1):
        k1=h*du (x_0,y_0)
        k2=h*du (x_0+h/2,y_0+k1/2)
        k3=h*du (x_0+h/2,y_0+k2/2)
        k4=h*du (x_0+h,y_0+k3)
        y1=y_0+ (k1+2*k2+2*k3+k4) /6
        x_0=x_0+h
        y_0=y1
    
    return y1



def __main__():
    x0 = float(0);
    y0 = float(1);
    xk = float(1);
    n = 1;
    for i in range(33):
        print(str(i) + ". " + str(x0) + " " + str(rutte(x0,y0,xk,n)) + " " + str(euler(x0,y0,xk,n)) + " " + str(abs(rutte(x0,y0,xk,n) - euler(x0,y0,xk,n))))
        x0 += float(1/32)
        y0 == rutte(x0,y0,xk,n)
        n += 1
    

if (__name__ == "__main__"):
    __main__()