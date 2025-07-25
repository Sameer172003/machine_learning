# What is Feature Scaling (Standardization)?

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset=dataset=pd.read_csv("C:\\Users\\ojhas\\Dropbox\\PC\\Downloads\\test_data.csv")
# print(dataset)
dataset["Age"].fillna(dataset["Age"].mode()[0],inplace=True)
# print(dataset)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()

dataset["Age_ss"]=pd.DataFrame(ss.fit_transform(dataset[["Age"]]),columns=["X"])

# print(dataset)
plt.subplot(1,2,1)
plt.title("Before")
sns.distplot(dataset["Age_ss"])

plt.subplot(1,2,2)
plt.title("After")
sns.distplot(dataset["Age"])

plt.show()