import pandas as pd                        
from pytrends.request import TrendReq
import datetime

#initiate instance for trends in England
pytrend = TrendReq(hl='GB-ENG', tz=360)

#use Southampton FC as the google trends keywords
kw_list = ['Southampton Football Club']

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
pytrend.build_payload(kw_list=kw_list, timeframe=f"{year} {today}", geo='GB-ENG', cat=0)
all_df = pytrend.interest_over_time()
all_df = all_df.drop('isPartial', axis = 1).rename(columns={'Southampton Football Club':'All'})

#loop through remaining categories
for key in categories:
    try:
        pytrend.build_payload(kw_list=kw_list, timeframe=f"{year} {today}", geo='US-IL', cat=categories[key])
        data = pytrend.interest_over_time()
        data = data.drop('isPartial', axis = 1).rename(columns={'Southampton Football Club':key})
        all_df = pd.concat([all_df, data], axis = 1)
    except:
        continue
