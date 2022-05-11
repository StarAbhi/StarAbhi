import numpy as np
import matplotlib.pyplot as plt
class diff:
    def init (self,f):
        self.diff1=(f(x+h)-f(x))/h
        self.diff2=(f(x+h)-f(x-h))/(2*h)
        self.diff3=(-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

    def f(x):
        return np.sin(2*np.pi*x)
    def exact_derivative(x):
        return 2*np.pi*np.cos(2*np.pi*x)
    def plot_graph():
        plt.plot(x, d.diff1,label="diff1")
        plt.plot(x, d.diff2, label="diff2")
        plt.plot(x, d.diff3, label="diff3")
        plt.plot(x, exact_derivative(x), label="exact")
        plt.legend(loc="lower right")
        plt.title("grafh for h={}".format(h))
        plt.show()

x = np.arange(-1,1.1,0.1)

h=0.9
d=diff(h)
d.plot_graph()

h=0.6
d=diff(h)
d.plot_graph()

h=0.3
d=diff(h)
d.plot_graph()

h=0.1
d=diff(h)
d.plot_graph()