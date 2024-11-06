import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dataframe = pd.read_excel("C:/Users/RueDr/Desktop/dataset.ods", header=1)

num_dataframe = dataframe.select_dtypes(include=['float64', 'int64'])

heatmap = num_dataframe.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap, annot=True, cmap="Purples", center = 0)
plt.title("- - - - - Heatmap - - - - -")
plt.show()
