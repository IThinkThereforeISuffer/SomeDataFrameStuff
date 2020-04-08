import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

most_visits = ad_clicks.groupby('utm_source').user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id')

number_people = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()


clicks_group_pivot = clicks_by_group.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id')

number_people = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

a_by_day = a_clicks.groupby(["day", "is_click"]).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id')
a_by_day.columns = ["clicked", "not_clicked"]
a_by_day["percent_click_day"] = a_by_day.clicked/(a_by_day.clicked + a_by_day.not_clicked)

b_by_day = b_clicks.groupby(["day", "is_click"]).user_id.count().reset_index().pivot(columns = 'is_click', index = 'day', values = 'user_id')
b_by_day.columns = ["clicked", "not_clicked"]
b_by_day["percent_click_day"] = b_by_day.clicked/(b_by_day.clicked + b_by_day.not_clicked)

df = pd.DataFrame()
df['percent_A'] = a_by_day.percent_click_day
df['percent_B'] = b_by_day.percent_click_day
print(df)
