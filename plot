import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=pd.read_csv("活頁簿2.csv",engine="python",encoding="utf-8")

plt.scatter(a["Unnamed: 0"], a["SI07"])
plt.scatter(a["Unnamed: 0"], a["SI06"])
plt.scatter(a["Unnamed: 0"], a["SI05"])
plt.scatter(a["Unnamed: 0"], a["SI04"])
plt.scatter(a["Unnamed: 0"], a["SI03"])
plt.scatter(a["Unnamed: 0"], a["SI02"])
plt.scatter(a["Unnamed: 0"], a["SI01"])
plt.scatter(a["Unnamed: 0"], a["SI00"])
plt.legend()
plt.xlabel("date")
plt.ylabel("count")
plt.show()
