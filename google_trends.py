import pandas as pd                        
from pytrends.request import TrendReq
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#initiate instance for trends in England
pytrend = TrendReq(hl='en-US', tz=360)

#use Manchester United FC as the google trends keywords
kw_list = ['Manchester United']

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
all_df = all_df.drop('isPartial', axis = 1).rename(columns={'Manchester United':'All'})

#loop through remaining categories
for key in categories:
    try:
        pytrend.build_payload(kw_list=kw_list, timeframe=f"{year} {today}", geo='US-IL', cat=categories[key])
        data = pytrend.interest_over_time()
        data = data.drop('isPartial', axis = 1).rename(columns={'Manchester United':key})
        all_df = pd.concat([all_df, data], axis = 1)
    except:
        continue

plt.figure(figsize=(12, 6))
plt.plot(all_df.index, all_df['Sports News'], label='Sports News')
#plt.plot(all_df.index, all_df['Sports'], label='Sports')
#plt.plot(all_df.index, all_df['Team Sports'], label='Team Sports')
plt.plot(all_df.index, all_df['Soccer'], label='Soccer')
plt.xlabel('Date', size=12)
plt.ylabel('Google Trend Indicator', size=12)
plt.title('Manchester United FC Google Trends\n(America)', size=14)
plt.legend()
plt.show()
