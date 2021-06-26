import  pandas as pd 
import csv 
import plotly.figure_factory as ff

df= pd.read_csv("Height.csv")
graph = ff.create_distplot([df["Height(Inches)"].tolist()], ["Height"])
