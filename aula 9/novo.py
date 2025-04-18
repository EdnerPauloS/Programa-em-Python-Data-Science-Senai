import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [100,20,500,400,300]
y = ['A','B','C','D','E']

df = pd.read_csv('dados.csv')
dados = pd.DataFrame(df)


plt.pie(x,labels=y, autopct='%2.2f%%')
plt.show()