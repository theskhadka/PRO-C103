import pandas as pd
import plotly.express as px

df = pd.read_csv("PRO-C103DATA.csv")
fig = px.scatter(df, x = "date", y =  "cases", color = "country", title = "cases", size_max = 60)
fig.show()