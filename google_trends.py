import pandas as pd                        
from pytrends.request import TrendReq
import datetime

#initiate instance for trends in the US
pytrend = TrendReq(hl='en-US', tz=360)

#use Chicago Fire FC as the google trends keywords
kw_list = ['Chicago Fire FC']

#get dates for time range
#Specify date ranges here
year = (datetime.date(datetime.date.today().year, 1, 1)).strftime('%Y-%m-%d')
today = datetime.date.today().strftime('%Y-%m-%d')

#categories for trending comparison
categories = {'Sports News': 1077,
              'Sports': 20,
              'Team Sports': 1001,
              'Soccer':294}

#get information for all categories
pytrend.build_payload(kw_list=kw_list, timeframe=f"{year} {today}", geo='US-IL', cat=0)
all_df = pytrend.interest_over_time()
all_df = all_df.drop('isPartial', axis = 1).rename(columns={'Chicago Fire FC':'All'})

#loop through remaining categories
for key in categories:
    try:
        pytrend.build_payload(kw_list=kw_list, timeframe=f"{year} {today}", geo='US-IL', cat=categories[key])
        data = pytrend.interest_over_time()
        data = data.drop('isPartial', axis = 1).rename(columns={'Chicago Fire FC':key})
        all_df = pd.concat([all_df, data], axis = 1)
    except:
        continue
