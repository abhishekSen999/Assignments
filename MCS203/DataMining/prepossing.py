import pandas as pd
data=pd.read_csv("data.csv")
print (data.T)
(data.T).to_csv("transpose.csv")

