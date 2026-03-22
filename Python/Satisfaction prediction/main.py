import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["Indicator"] == "Life satisfaction"]

    # Some datasets have "Value" without "Measure"
    if "Measure" in oecd_bli.columns:
        oecd_bli = oecd_bli.pivot_table(index="Country", values="Value", aggfunc='mean')
    else:
        oecd_bli = oecd_bli.set_index("Country")["Value"]
        oecd_bli = oecd_bli.to_frame()

    oecd_bli.rename(columns={"Value": "Life satisfaction"}, inplace=True)
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(oecd_bli, gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    return full_country_stats[["GDP per capita", "Life satisfaction"]]
oecd_bli=pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita=pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t', encoding='latin1', na_values="n/a")
country_stats=prepare_country_stats(oecd_bli, gdp_per_capita)
x=np.c_[country_stats["GDP per capita"]]
y=np.c_[country_stats["Life satisfaction"]]
model=sklearn.linear_model.LinearRegression()

model.fit(x,y)
print(model.predict([[22587]]))
country_stats.plot(kind='scatter', x="GDP per capita", y="Life satisfaction")
plt.plot(x, model.predict(x), color='red')  
plt.show()

