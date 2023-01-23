import time, sys
from sklearn.datasets import fetch_california_housing

def delay_print(w):
    for s in w:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(.05)

house_prices = fetch_california_housing()
digits = datasetsi.load_digits()

print(house_prices)
delay_print('|                       |\n')

print(house_prices.target)
delay_print('|                       |\n')

print(house_prices.data)
delay_print('|                       |\n')


