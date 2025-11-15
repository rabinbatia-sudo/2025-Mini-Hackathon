import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"countypres_2000-2024.csv")
df2 = df.copy()
df2 = df2.drop(columns = ['office', 'state'])

x = df2.groupby(['year', 'state_po', 'county_name', 'candidate', 'party'])['candidatevotes'].sum()
x = x.reset_index()
y = pd.DataFrame(x)
y['result'] = ' '

x = y.groupby(['year', 'state_po', 'county_name'])['candidatevotes'].max()
x = pd.DataFrame(x)

fina_df = pd.merge(x, y, on = ['year', 'state_po', 'county_name'])
fina_df['total_votes_of_winner'] = fina_df['candidatevotes_x']
fina_df['candidatevotes'] = fina_df['candidatevotes_y']
fina_df = fina_df.drop(columns = ['candidatevotes_y', 'candidatevotes_x'])
fina_df['result'] = (fina_df['total_votes_of_winner'] == fina_df['candidatevotes']).astype(int)



final_df = fina_df.drop(columns = 'total_votes_of_winner')

states = final_df.groupby(['year', 'state_po', 'candidate', 'party'])['candidatevotes'].sum()
states = pd.DataFrame(states)
states = states.reset_index()

years = final_df.groupby(['year', 'candidate', 'party'])['candidatevotes'].sum()
years = pd.DataFrame(years)
years = years.reset_index()

years_dict = {2000:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0.05, 0, 0, 0]},
              2004:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0.05, 0, 0]},
              2008:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0.05, 0, 0]},
              2012:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0.05, 0, 0]},
              2016:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0, 0.05, 0]},
              2020:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0, 0, 0.05, 0, 0]},
              2024:{"candidates":[], "parties":[], "votes":[], "colors":[], "explode":[0, 0.05, 0, 0]}}

for i, row in years.iterrows():
  for x in years_dict:
    if row[0] == x and (row[1] != "OVERVOTES" and row[1] != "UNDERVOTES"):
      years_dict[x]["candidates"].append(row[1])
      years_dict[x]["parties"].append(row[2])
      years_dict[x]["votes"].append(row[3])
      if row[2] == "DEMOCRAT":
        years_dict[x]["colors"].append("CornflowerBlue")
      elif row[2] == "REPUBLICAN":
        years_dict[x]["colors"].append("Crimson")
      elif row[2] == "GREEN":
        years_dict[x]["colors"].append("DarkGreen")
      elif row[2] == "LIBERTARIAN":
        years_dict[x]["colors"].append("DarkGray")
      else:
        years_dict[x]["colors"].append("BurlyWood")

years_states = {2000:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2004:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2008:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2012:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2016:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2020:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}, 
                2024:{"AL":{}, "AK":{}, "AZ":{}, "AR":{}, "CA":{}, "CO":{}, "CT":{}, "DE":{}, "DC":{}, "FL":{}, "GA":{}, "HI":{}, "ID":{}, "IL":{}, "IN":{}, "IA":{}, "KS":{}, "KY":{}, "LA":{},
          "ME":{}, "MD":{}, "MA":{}, "MI":{}, "MN":{}, "MS":{}, "MO":{}, "MT":{}, "NE":{}, "NV":{}, "NH":{}, "NJ":{}, "NM":{}, "NY":{}, "NC":{}, "ND":{}, "OH":{}, "OK":{}, "OR":{}, 
          "PA":{}, "RI":{}, "SC":{}, "SD":{}, "TN":{}, "TX":{}, "UT":{}, "VT":{}, "VA":{}, "WA":{}, "WV":{}, "WI":{}, "WY":{}}}

for i, row in final_df.iterrows():
  for x in years_states:
    ""
  

for x in years_dict:
  fig, ax = plt.subplots()
  ax.set_title(f"{x} Election")
  ax.pie(years_dict[x]["votes"],
         labels= years_dict[x]["candidates"],
         colors=years_dict[x]["colors"],
         explode=years_dict[x]["explode"],
         autopct='%1.1f%%')
  ax.legend(years_dict[x]["votes"],
            title="Number of Votes",
            loc="center left",
            bbox_to_anchor=(1.2, 0, 0.5, 1))
  plt.show()