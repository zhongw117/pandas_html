# -×-Coding: utf8 -*-
import pandas as pd

property_df,  = pd.read_html("http://kanview.ks.gov/PayRates/PayRates_Agency.aspx", header=0, )

print(property_df)