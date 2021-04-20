import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import seaborn as sns

df=pd.read_csv("bankdata.csv")
df.head()
print(df)

print(df["age"].min())

print(df["age"].max())

print(df["age"].mean())

print(df["job"].value_counts())

print(df["poutcome"].value_counts())

print(df["month"].value_counts())

print(df.groupby(["job"])["age"].mean())

print(df["education"].value_counts())

print(df["age"].tolist)

list_of_jobs = df["job"].values.tolist()
print(" list of jobs: ",list_of_jobs)

print(list(dict.fromkeys(list_of_jobs)))

# Analysing and visualizing the data

print(df.describe())
print(df.info())

f, ax = plt.subplots(1,2, figsize=(16,8))

colors = ["#FA5858", "#64FE2E"]
labels ="Did not Open Term Suscriptions", "Opened Term Suscriptions"

plt.suptitle('Information on Term Suscriptions', fontsize=20)

df["deposit"].value_counts().plot.pie(explode=[0,0.25], autopct='%1.2f%%', ax=ax[0], shadow=True, colors=colors,
                                             labels=labels, fontsize=12, startangle=25)


# ax[0].set_title('State of Loan', fontsize=16)
ax[0].set_ylabel('% of Condition of Loans', fontsize=14)
# sns.countplot('loan_condition', data=df, ax=ax[1], palette=colors)
# ax[1].set_title('Condition of Loans', fontsize=20)
# ax[1].set_xticklabels(['Good', 'Bad'], rotation='horizontal')
palette = ["#64FE2E", "#FA5858"]

sns.barplot(x="education", y="balance", hue="deposit", data=df, palette=palette, estimator=lambda x: len(x) / len(df) * 100)
ax[1].set(ylabel="(%)")
ax[1].set_xticklabels(df["education"].unique(), rotation=0, rotation_mode="anchor")
plt.show()

# Numeric data is distribution
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

df.hist(bins=20, figsize=(14,10), color='#E14906')
plt.show()

print(df['deposit'].value_counts())

print(df.columns)

#analysing the marital status
print(df['marital'].value_counts())

df['marital'].unique()
df['marital'].value_counts().tolist()

print (df.sort_values(["age"]))

print(df["poutcome"])

df.drop(['previous'], axis='columns', inplace=True)
print(df)

#campaign outcomes
positive = "success"
negative= "failure"
unknown = "unknown"

campaign_outcomes= [positive,negative,unknown]
print(campaign_outcomes)

print(df[df["poutcome"]=="success"])

import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

slices = [8326,1228,1071,537]
labels= ["unknown","failure","success","other"]
colors= ["#008fd5", "#fc4f30", "#e5ae37", "#6d904f"]
plt.pie(slices,labels=labels, colors=colors, wedgeprops={"edgecolor": "black"})

plt.title("Campaign outcomes")
plt.tight_layout()
plt.show()


















