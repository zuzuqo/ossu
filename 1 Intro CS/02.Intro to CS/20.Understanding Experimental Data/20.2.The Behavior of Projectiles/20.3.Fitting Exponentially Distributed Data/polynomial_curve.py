import matplotlib
import numpy as np
from matplotlib import pyplot as plt

vals = []
for i in range(10):
    vals.append(3 ** i)

matplotlib.use('TkAgg')

plt.plot(vals, 'ko', label='Actual points')
x_vals = np.arange(10)
fit = np.polyfit(x_vals, vals, 5)
y_vals = np.polyval(fit, x_vals)
plt.plot(y_vals, 'kx', label='Predicted points', markeredgewidth=2, markersize=25)
plt.title('Fitting y=3**x')
plt.legend(loc='upper left')
plt.show()

print(f'Model predicts that 3**20 is roughly {np.polyval(fit, [3 ** 20])[0]}')
print(f'Actual value of 3**20 is {3 ** 20}')
