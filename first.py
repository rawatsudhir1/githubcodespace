import matplotlib.pyplot as plt
import numpy as np

gen_value = np.arange(0.0, 2.0, 0.01)
sinval = 1 + np.sin(2*np.pi*gen_value)
plt.plot(gen_value, sinval)

plt.xlabel('time (sinval)')
plt.ylabel('voltage (mV)')
plt.title('Devops Virtual Summit...github codespace demo')
plt.grid(True)
plt.savefig("test.png")
