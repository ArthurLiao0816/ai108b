import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4, suppress=True)
freq = random.randint(0,4) #設定頻率
t = np.arange(0, 10, 0.1)   #設定取樣範圍、取樣區間
ft = 10*np.cos(2*np.pi*freq*t) #10*cos(2*pi*f*t)
n = len(ft)
t1 = t[range(int(n/2))]
fi = np.fft.fft(ft)

fi1 = fi[range(int(n/2))]
print('ft=', ft)
print('fi=', fi)
print('freq= ', freq)

fig, ax = plt.subplots(2, 1)

ax[0].plot(t,ft, color="red", linewidth=2)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
 
ax[1].plot(t1,fi1, color="blue", linewidth=2)
ax[1].set_xlabel('freq')
ax[1].set_ylabel('y')

plt.show()
