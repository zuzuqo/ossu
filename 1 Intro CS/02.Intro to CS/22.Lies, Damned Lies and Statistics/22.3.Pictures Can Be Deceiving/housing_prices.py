import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_housing(impression):
    labels, prices = ([], [])
    with open('houses.csv') as file:
        for line in file:
            year, quarter, price = line.split(',')
            label = f'{year[2:4]}\n Q{quarter[1]}'
            labels.append(label)
            prices.append(int(price)/1000)
    quarters = np.arange(len(labels))
    width = 0.8
    matplotlib.use('TkAgg')
    plt.bar(quarters, prices, width)
    plt.xticks(quarters+width/2, labels)
    plt.title('Housing Prices in US Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    plt.show()
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError

if __name__ == '__main__':
    plot_housing('flat')
    plot_housing('volatile')
    plot_housing('fair')
