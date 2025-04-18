import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names = ['group_a', 'group_b', 'group_c', 'd']
values = [1, 10, 100, 400]

plt.figure(figsize=(12,4))

plt.subplot(241)
plt.bar(names, values)

plt.subplot(242)
plt.plot(names, values)

plt.subplot(243)
plt.pie( values, labels=values, autopct='%1.1f%%')

plt.subplot(244)
plt.scatter(values, values)


plt.subplot(245)
plt.bar(names, values)

plt.subplot(246)
plt.plot(names, values)

plt.subplot(247)
plt.pie( values, labels=values)

plt.subplot(248)
plt.scatter(values, values)



plt.show()