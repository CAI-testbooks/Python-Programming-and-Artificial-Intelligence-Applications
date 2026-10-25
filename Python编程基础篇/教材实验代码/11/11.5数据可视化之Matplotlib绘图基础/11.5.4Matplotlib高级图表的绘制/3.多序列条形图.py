import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = {'series1' : [1, 3, 4, 5, 5], 'series2' : [2, 4, 5, 3, 3], 'series3': [3, 4, 3 ,2 ,1]}
df = pd.DataFrame(data)
df.plot(kind = 'bar')
plt.show()