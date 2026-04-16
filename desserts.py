import numpy as np
import pandas as pd

desserts=pd.read_excel(r'/Users/theofunk/Desktop/classes/200c/favorite_desserts/desserrtts.xlsx')


avg_count=np.mean(desserts['count'])

print(avg_count)